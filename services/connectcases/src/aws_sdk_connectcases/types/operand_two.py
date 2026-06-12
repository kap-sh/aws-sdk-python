"""Generated from Smithy shape ``com.amazonaws.connectcases#OperandTwo``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_connectcases.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.empty_operand_value


class _OperandTwo_stringValue(TypedDict):
    stringValue: "str"


class _OperandTwo_booleanValue(TypedDict):
    booleanValue: "bool"


class _OperandTwo_doubleValue(TypedDict):
    doubleValue: "float"


class _OperandTwo_emptyValue(TypedDict):
    emptyValue: "aws_sdk_connectcases.types.empty_operand_value.EmptyOperandValue"


OperandTwo: TypeAlias = (
    _OperandTwo_stringValue
    | _OperandTwo_booleanValue
    | _OperandTwo_doubleValue
    | _OperandTwo_emptyValue
)


# --- restJson1 ser/de ---
def serialize_json(value: OperandTwo) -> dict:
    if "stringValue" in value:
        return {"stringValue": value["stringValue"]}
    elif "booleanValue" in value:
        return {"booleanValue": value["booleanValue"]}
    elif "doubleValue" in value:
        return {"doubleValue": value["doubleValue"]}
    elif "emptyValue" in value:
        import aws_sdk_connectcases.types.empty_operand_value

        return {
            "emptyValue": aws_sdk_connectcases.types.empty_operand_value.serialize_json(
                value["emptyValue"]
            )
        }
    else:
        raise SerializationError("OperandTwo: no variant present")


def deserialize_json(data: dict) -> OperandTwo:
    if "stringValue" in data:
        return {"stringValue": data["stringValue"]}
    elif "booleanValue" in data:
        return {"booleanValue": data["booleanValue"]}
    elif "doubleValue" in data:
        return {"doubleValue": data["doubleValue"]}
    elif "emptyValue" in data:
        import aws_sdk_connectcases.types.empty_operand_value

        return {
            "emptyValue": aws_sdk_connectcases.types.empty_operand_value.deserialize_json(
                data["emptyValue"]
            )
        }
    else:
        raise DeserializationError("OperandTwo: no recognized variant key")
