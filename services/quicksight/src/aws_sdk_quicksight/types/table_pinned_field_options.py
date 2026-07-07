"""Generated from Smithy shape ``com.amazonaws.quicksight#TablePinnedFieldOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.table_field_order_list


class TablePinnedFieldOptions(TypedDict, closed=True):
    pinned_left_fields: NotRequired[
        "aws_sdk_quicksight.types.table_field_order_list.TableFieldOrderList"
    ]
    """<p>A list of columns to be pinned to the left of a table visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TablePinnedFieldOptions) -> dict:
    out: dict = {}
    if "pinned_left_fields" in value:
        import aws_sdk_quicksight.types.table_field_order_list

        out["PinnedLeftFields"] = (
            aws_sdk_quicksight.types.table_field_order_list.serialize_json(
                value["pinned_left_fields"]
            )
        )
    return out


def deserialize_json(data: dict) -> TablePinnedFieldOptions:
    out: TablePinnedFieldOptions = {}  # type: ignore[typeddict-item]
    if "PinnedLeftFields" in data:
        import aws_sdk_quicksight.types.table_field_order_list

        out["pinned_left_fields"] = (
            aws_sdk_quicksight.types.table_field_order_list.deserialize_json(
                data["PinnedLeftFields"]
            )
        )
    return out
