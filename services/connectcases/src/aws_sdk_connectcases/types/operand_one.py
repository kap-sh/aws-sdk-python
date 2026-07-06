"""Generated from Smithy shape ``com.amazonaws.connectcases#OperandOne``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_connectcases.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.field_id


class _OperandOne_fieldId(TypedDict, closed=True):
    fieldId: "aws_sdk_connectcases.types.field_id.FieldId"


OperandOne: TypeAlias = _OperandOne_fieldId


# --- restJson1 ser/de ---
def serialize_json(value: OperandOne) -> dict:
    if "fieldId" in value:
        return {"fieldId": value["fieldId"]}
    else:
        raise SerializationError("OperandOne: no variant present")


def deserialize_json(data: dict) -> OperandOne:
    if "fieldId" in data:
        return {"fieldId": data["fieldId"]}
    else:
        raise DeserializationError("OperandOne: no recognized variant key")
