"""Generated from Smithy shape ``com.amazonaws.quicksight#FilledMapSortConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.field_sort_options_list


class FilledMapSortConfiguration(TypedDict):
    category_sort: NotRequired[
        "aws_sdk_quicksight.types.field_sort_options_list.FieldSortOptionsList"
    ]
    """<p>The sort configuration of the location fields.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilledMapSortConfiguration) -> dict:
    out: dict = {}
    if "category_sort" in value:
        import aws_sdk_quicksight.types.field_sort_options_list

        out["CategorySort"] = (
            aws_sdk_quicksight.types.field_sort_options_list.serialize_json(
                value["category_sort"]
            )
        )
    return out


def deserialize_json(data: dict) -> FilledMapSortConfiguration:
    out: FilledMapSortConfiguration = {}  # type: ignore[typeddict-item]
    if "CategorySort" in data:
        import aws_sdk_quicksight.types.field_sort_options_list

        out["category_sort"] = (
            aws_sdk_quicksight.types.field_sort_options_list.deserialize_json(
                data["CategorySort"]
            )
        )
    return out
