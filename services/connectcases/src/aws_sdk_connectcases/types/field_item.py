"""Generated from Smithy shape ``com.amazonaws.connectcases#FieldItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.field_id


class FieldItem(TypedDict, closed=True):
    id: "aws_sdk_connectcases.types.field_id.FieldId"
    """<p>Unique identifier of a field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FieldItem) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> FieldItem:
    out: FieldItem = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("FieldItem.id required")
    return out
