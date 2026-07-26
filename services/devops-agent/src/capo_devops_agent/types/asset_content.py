"""Generated from Smithy shape ``com.amazonaws.devopsagent#AssetContent``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.asset_file_content
    import capo_devops_agent.types.asset_zip_content


class _AssetContent_file(TypedDict, closed=True):
    file: "capo_devops_agent.types.asset_file_content.AssetFileContent"


class _AssetContent_zip(TypedDict, closed=True):
    zip: "capo_devops_agent.types.asset_zip_content.AssetZipContent"


AssetContent: TypeAlias = _AssetContent_file | _AssetContent_zip


# --- restJson1 ser/de ---
def serialize_json(value: AssetContent) -> dict:
    if "file" in value:
        import capo_devops_agent.types.asset_file_content

        return {
            "file": capo_devops_agent.types.asset_file_content.serialize_json(
                value["file"]
            )
        }
    elif "zip" in value:
        import capo_devops_agent.types.asset_zip_content

        return {
            "zip": capo_devops_agent.types.asset_zip_content.serialize_json(
                value["zip"]
            )
        }
    else:
        raise SerializationError("AssetContent: no variant present")


def deserialize_json(data: dict) -> AssetContent:
    if "file" in data:
        import capo_devops_agent.types.asset_file_content

        return {
            "file": capo_devops_agent.types.asset_file_content.deserialize_json(
                data["file"]
            )
        }
    elif "zip" in data:
        import capo_devops_agent.types.asset_zip_content

        return {
            "zip": capo_devops_agent.types.asset_zip_content.deserialize_json(
                data["zip"]
            )
        }
    else:
        raise DeserializationError("AssetContent: no recognized variant key")
