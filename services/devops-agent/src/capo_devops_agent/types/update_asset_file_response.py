"""Generated from Smithy shape ``com.amazonaws.devopsagent#UpdateAssetFileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.asset_file


class UpdateAssetFileResponse(TypedDict, closed=True):
    file: "capo_devops_agent.types.asset_file.AssetFile"
    """<p>The asset file object</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAssetFileResponse) -> dict:
    out: dict = {}
    import capo_devops_agent.types.asset_file

    out["file"] = capo_devops_agent.types.asset_file.serialize_json(value["file"])
    return out


def deserialize_json(data: dict) -> UpdateAssetFileResponse:
    out: UpdateAssetFileResponse = {}  # type: ignore[typeddict-item]
    if "file" in data:
        import capo_devops_agent.types.asset_file

        out["file"] = capo_devops_agent.types.asset_file.deserialize_json(data["file"])
    else:
        raise DeserializationError("UpdateAssetFileResponse.file required")
    return out
