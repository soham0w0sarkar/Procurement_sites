document.addEventListener('DOMContentLoaded', function() {
  // Add new empty form
  document.getElementById('add-item').addEventListener('click', function() {
      const formCount = parseInt(document.getElementById('id_orderitem_set-TOTAL_FORMS').value);
      const container = document.getElementById('order-items');
      
      // Clone first empty form
      const newForm = container.children[0].cloneNode(true);
      
      // Update form attributes
      newForm.innerHTML = newForm.innerHTML.replace(/__prefix__/g, formCount);
      document.getElementById('id_orderitem_set-TOTAL_FORMS').value = formCount + 1;
      
      // Clear values and show
      newForm.querySelector('input[name$="-product"]').value = '';
      newForm.querySelector('input[name$="-quantity"]').value = '1';
      newForm.querySelector('h6').textContent = '';
      newForm.querySelector('.text-muted').textContent = '';
      newForm.querySelector('.remove-item').style.display = 'block';
      
      container.appendChild(newForm);
  });

  // Remove item
  document.addEventListener('click', function(e) {
      if (e.target.classList.contains('remove-item')) {
          const form = e.target.closest('.order-item-form');
          if (form.querySelector('input[name$="-DELETE"]')) {
              form.querySelector('input[name$="-DELETE"]').value = 'on';
              form.style.display = 'none';
          } else {
              form.remove();
          }
      }
  });
});