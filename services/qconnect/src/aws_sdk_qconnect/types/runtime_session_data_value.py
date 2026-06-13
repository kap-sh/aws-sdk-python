"""Generated from Smithy shape ``com.amazonaws.qconnect#RuntimeSessionDataValue``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_qconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.non_empty_sensitive_string


class _RuntimeSessionDataValue_stringValue(TypedDict):
    stringValue: (
        "aws_sdk_qconnect.types.non_empty_sensitive_string.NonEmptySensitiveString"
    )


RuntimeSessionDataValue: TypeAlias = _RuntimeSessionDataValue_stringValue


# --- restJson1 ser/de ---
def serialize_json(value: RuntimeSessionDataValue) -> dict:
    if "stringValue" in value:
        return {"stringValue": value["stringValue"]}
    else:
        raise SerializationError("RuntimeSessionDataValue: no variant present")


def deserialize_json(data: dict) -> RuntimeSessionDataValue:
    if "stringValue" in data:
        return {"stringValue": data["stringValue"]}
    else:
        raise DeserializationError("RuntimeSessionDataValue: no recognized variant key")
