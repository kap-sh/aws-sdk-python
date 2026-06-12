"""Generated from Smithy shape ``com.amazonaws.b2bi#InputFileSource``."""

from typing import TypeAlias, TypedDict

from aws_sdk_b2bi.errors import DeserializationError, SerializationError


class _InputFileSource_fileContent(TypedDict):
    fileContent: "str"


InputFileSource: TypeAlias = _InputFileSource_fileContent


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InputFileSource) -> dict:
    if "fileContent" in value:
        return {"fileContent": value["fileContent"]}
    else:
        raise SerializationError("InputFileSource: no variant present")


def deserialize_aws_json_1_0(data: dict) -> InputFileSource:
    if "fileContent" in data:
        return {"fileContent": data["fileContent"]}
    else:
        raise DeserializationError("InputFileSource: no recognized variant key")
