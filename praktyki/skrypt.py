from bs4 import BeautifulSoup

def extract_book_info(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    books = soup.find_all('div', class_='book')

    book_info = []
    total_price = 0
    for book in books:
        title = book.find(class_='book-info').text.strip()
        price = float(book.find('span', class_='price price-incart').text.strip().replace('$', ''))
        total_price += price
        book_info.append({'book-info': title, 'price price-incart': price})

    avg_price = total_price / len(book_info)
    
    return book_info


all_books, expensive_books = extract_book_info(html_content)
print("Wszystkie książki:")
for book in all_books:
    print(f"Tytuł: {book['title']}, Cena: ${book['price']}")

