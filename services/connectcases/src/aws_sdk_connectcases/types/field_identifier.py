"""Generated from Smithy shape ``com.amazonaws.connectcases#FieldIdentifier``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.field_id


class FieldIdentifier(TypedDict):
    id: "aws_sdk_connectcases.types.field_id.FieldId"
    """<p>Unique identifier of a field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FieldIdentifier) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> FieldIdentifier:
    out: FieldIdentifier = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("FieldIdentifier.id required")
    return out
