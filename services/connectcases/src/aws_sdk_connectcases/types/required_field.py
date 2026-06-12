"""Generated from Smithy shape ``com.amazonaws.connectcases#RequiredField``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.field_id


class RequiredField(TypedDict):
    field_id: "aws_sdk_connectcases.types.field_id.FieldId"
    """<p>Unique identifier of a field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RequiredField) -> dict:
    out: dict = {}
    out["fieldId"] = value["field_id"]
    return out


def deserialize_json(data: dict) -> RequiredField:
    out: RequiredField = {}  # type: ignore[typeddict-item]
    if "fieldId" in data:
        out["field_id"] = data["fieldId"]
    else:
        raise DeserializationError("RequiredField.field_id required")
    return out
