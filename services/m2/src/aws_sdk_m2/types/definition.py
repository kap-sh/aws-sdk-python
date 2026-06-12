"""Generated from Smithy shape ``com.amazonaws.m2#Definition``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_m2.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_m2.types.string2000
    import aws_sdk_m2.types.string_free65000


class _Definition_s3Location(TypedDict):
    s3Location: "aws_sdk_m2.types.string2000.String2000"


class _Definition_content(TypedDict):
    content: "aws_sdk_m2.types.string_free65000.StringFree65000"


Definition: TypeAlias = _Definition_s3Location | _Definition_content


# --- restJson1 ser/de ---
def serialize_json(value: Definition) -> dict:
    if "s3Location" in value:
        return {"s3Location": value["s3Location"]}
    elif "content" in value:
        return {"content": value["content"]}
    else:
        raise SerializationError("Definition: no variant present")


def deserialize_json(data: dict) -> Definition:
    if "s3Location" in data:
        return {"s3Location": data["s3Location"]}
    elif "content" in data:
        return {"content": data["content"]}
    else:
        raise DeserializationError("Definition: no recognized variant key")
