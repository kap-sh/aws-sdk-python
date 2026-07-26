"""Generated from Smithy shape ``com.amazonaws.connectcases#CreateFieldResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connectcases.types.field_arn
    import capo_connectcases.types.field_id


class CreateFieldResponse(TypedDict, closed=True):
    field_id: "capo_connectcases.types.field_id.FieldId"
    """<p>The unique identifier of a field.</p>"""
    field_arn: "capo_connectcases.types.field_arn.FieldArn"
    """<p>The Amazon Resource Name (ARN) of the field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFieldResponse) -> dict:
    out: dict = {}
    out["fieldId"] = value["field_id"]
    out["fieldArn"] = value["field_arn"]
    return out


def deserialize_json(data: dict) -> CreateFieldResponse:
    out: CreateFieldResponse = {}  # type: ignore[typeddict-item]
    if "fieldId" in data:
        out["field_id"] = data["fieldId"]
    else:
        raise DeserializationError("CreateFieldResponse.field_id required")
    if "fieldArn" in data:
        out["field_arn"] = data["fieldArn"]
    else:
        raise DeserializationError("CreateFieldResponse.field_arn required")
    return out
