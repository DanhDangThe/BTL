document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('input[type="checkbox"]').forEach((checkbox) => {
        checkbox.addEventListener('change', function () {
            if (this.checked) {
                const group = this.getAttribute('data-group');
                document.querySelectorAll(`input[type="checkbox"][data-group="${group}"]`).forEach((box) => {
                    if (box !== this) {
                        box.checked = false;
                    }
                });
            }
        });
    });
});
