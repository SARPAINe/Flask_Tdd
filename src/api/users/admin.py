# src/api/users/admin.py


from flask_admin.contrib.sqla import ModelView


class UsersAdminView(ModelView):
    column_searchable_list = (
        "username",
        "email",
    )
    column_editable_list = (
        "username",
        "email",
        "created_date",
    )
    column_filters = (
        "username",
        "email",
    )
    column_sortable_list = (
        "username",
        "email",
        "active",
        "created_date",
    )
    # true is used for sorting in descending order
    column_default_sort = ("email", False)
