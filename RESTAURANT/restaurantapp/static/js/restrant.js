fetch("/menu/")
  .then(response => response.json())
  .then(data => {
    data.menu.forEach(item => {
      // Render menu items dynamically
    });
  });
