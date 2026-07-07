"""Generated from Smithy shape ``com.amazonaws.connectcases#Sort``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.field_id
    import aws_sdk_connectcases.types.order


class Sort(TypedDict, closed=True):
    field_id: "aws_sdk_connectcases.types.field_id.FieldId"
    """<p>Unique identifier of a field.</p>"""
    sort_order: "aws_sdk_connectcases.types.order.Order"
    """<p>A structured set of sort terms</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Sort) -> dict:
    out: dict = {}
    out["fieldId"] = value["field_id"]
    out["sortOrder"] = value["sort_order"]
    return out


def deserialize_json(data: dict) -> Sort:
    out: Sort = {}  # type: ignore[typeddict-item]
    if "fieldId" in data:
        out["field_id"] = data["fieldId"]
    else:
        raise DeserializationError("Sort.field_id required")
    if "sortOrder" in data:
        out["sort_order"] = data["sortOrder"]
    else:
        raise DeserializationError("Sort.sort_order required")
    return out
