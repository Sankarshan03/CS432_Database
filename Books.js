// Get all book items in the list
const bookItems = document.querySelectorAll('li');

// Loop through each book item
bookItems.forEach(item => {
    // Create book details elements
    const edition = document.createElement('p');
    const copies = document.createElement('p');
    const status = document.createElement('p');

    // Set book details text
    edition.textContent = 'Edition: 1st';
    copies.textContent = 'Copies: 3';
    status.textContent = 'Status: Available';

    // Add book details to book item
    item.appendChild(edition);
    item.appendChild(copies);
    item.appendChild(status);
});