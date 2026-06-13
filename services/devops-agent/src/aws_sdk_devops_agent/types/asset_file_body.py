"""Generated from Smithy shape ``com.amazonaws.devopsagent#AssetFileBody``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_devops_agent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.asset_file_bytes
    import aws_sdk_devops_agent.types.asset_file_text


class _AssetFileBody_bytes(TypedDict):
    bytes: "aws_sdk_devops_agent.types.asset_file_bytes.AssetFileBytes"


class _AssetFileBody_text(TypedDict):
    text: "aws_sdk_devops_agent.types.asset_file_text.AssetFileText"


AssetFileBody: TypeAlias = _AssetFileBody_bytes | _AssetFileBody_text


# --- restJson1 ser/de ---
def serialize_json(value: AssetFileBody) -> dict:
    if "bytes" in value:
        import aws_sdk_devops_agent.types.asset_file_bytes

        return {
            "bytes": aws_sdk_devops_agent.types.asset_file_bytes.serialize_json(
                value["bytes"]
            )
        }
    elif "text" in value:
        return {"text": value["text"]}
    else:
        raise SerializationError("AssetFileBody: no variant present")


def deserialize_json(data: dict) -> AssetFileBody:
    if "bytes" in data:
        import aws_sdk_devops_agent.types.asset_file_bytes

        return {
            "bytes": aws_sdk_devops_agent.types.asset_file_bytes.deserialize_json(
                data["bytes"]
            )
        }
    elif "text" in data:
        return {"text": data["text"]}
    else:
        raise DeserializationError("AssetFileBody: no recognized variant key")
