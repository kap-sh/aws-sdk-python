"""Generated from Smithy shape ``com.amazonaws.devopsagent#AssetFileBody``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.asset_file_bytes
    import capo_devops_agent.types.asset_file_text


class _AssetFileBody_bytes(TypedDict, closed=True):
    bytes: "capo_devops_agent.types.asset_file_bytes.AssetFileBytes"


class _AssetFileBody_text(TypedDict, closed=True):
    text: "capo_devops_agent.types.asset_file_text.AssetFileText"


AssetFileBody: TypeAlias = _AssetFileBody_bytes | _AssetFileBody_text


# --- restJson1 ser/de ---
def serialize_json(value: AssetFileBody) -> dict:
    if "bytes" in value:
        import capo_devops_agent.types.asset_file_bytes

        return {
            "bytes": capo_devops_agent.types.asset_file_bytes.serialize_json(
                value["bytes"]
            )
        }
    elif "text" in value:
        return {"text": value["text"]}
    else:
        raise SerializationError("AssetFileBody: no variant present")


def deserialize_json(data: dict) -> AssetFileBody:
    if "bytes" in data:
        import capo_devops_agent.types.asset_file_bytes

        return {
            "bytes": capo_devops_agent.types.asset_file_bytes.deserialize_json(
                data["bytes"]
            )
        }
    elif "text" in data:
        return {"text": data["text"]}
    else:
        raise DeserializationError("AssetFileBody: no recognized variant key")
