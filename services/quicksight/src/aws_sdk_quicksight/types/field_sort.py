"""Generated from Smithy shape ``com.amazonaws.quicksight#FieldSort``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.field_id
    import aws_sdk_quicksight.types.sort_direction


class FieldSort(TypedDict, closed=True):
    field_id: "aws_sdk_quicksight.types.field_id.FieldId"
    """<p>The sort configuration target field.</p>"""
    direction: "aws_sdk_quicksight.types.sort_direction.SortDirection"
    """<p>The sort direction. Choose one of the following options:</p> <ul> <li> <p> <code>ASC</code>: Ascending</p> </li> <li> <p> <code>DESC</code>: Descending</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: FieldSort) -> dict:
    out: dict = {}
    out["FieldId"] = value["field_id"]
    import aws_sdk_quicksight.types.sort_direction

    out["Direction"] = aws_sdk_quicksight.types.sort_direction.serialize_json(
        value["direction"]
    )
    return out


def deserialize_json(data: dict) -> FieldSort:
    out: FieldSort = {}  # type: ignore[typeddict-item]
    if "FieldId" in data:
        out["field_id"] = data["FieldId"]
    else:
        raise DeserializationError("FieldSort.field_id required")
    if "Direction" in data:
        import aws_sdk_quicksight.types.sort_direction

        out["direction"] = aws_sdk_quicksight.types.sort_direction.deserialize_json(
            data["Direction"]
        )
    else:
        raise DeserializationError("FieldSort.direction required")
    return out
