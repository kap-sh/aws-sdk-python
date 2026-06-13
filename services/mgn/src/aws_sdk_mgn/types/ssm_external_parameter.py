"""Generated from Smithy shape ``com.amazonaws.mgn#SsmExternalParameter``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_mgn.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_mgn.types.jmes_path_string


class _SsmExternalParameter_dynamicPath(TypedDict):
    dynamicPath: "aws_sdk_mgn.types.jmes_path_string.JmesPathString"


SsmExternalParameter: TypeAlias = _SsmExternalParameter_dynamicPath


# --- restJson1 ser/de ---
def serialize_json(value: SsmExternalParameter) -> dict:
    if "dynamicPath" in value:
        return {"dynamicPath": value["dynamicPath"]}
    else:
        raise SerializationError("SsmExternalParameter: no variant present")


def deserialize_json(data: dict) -> SsmExternalParameter:
    if "dynamicPath" in data:
        return {"dynamicPath": data["dynamicPath"]}
    else:
        raise DeserializationError("SsmExternalParameter: no recognized variant key")
