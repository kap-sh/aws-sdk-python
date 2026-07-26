"""Generated from Smithy shape ``com.amazonaws.devopsagent#CreateAssetFileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.asset_file


class CreateAssetFileResponse(TypedDict, closed=True):
    file: "capo_devops_agent.types.asset_file.AssetFile"
    """<p>The asset file object</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAssetFileResponse) -> dict:
    out: dict = {}
    import capo_devops_agent.types.asset_file

    out["file"] = capo_devops_agent.types.asset_file.serialize_json(value["file"])
    return out


def deserialize_json(data: dict) -> CreateAssetFileResponse:
    out: CreateAssetFileResponse = {}  # type: ignore[typeddict-item]
    if "file" in data:
        import capo_devops_agent.types.asset_file

        out["file"] = capo_devops_agent.types.asset_file.deserialize_json(data["file"])
    else:
        raise DeserializationError("CreateAssetFileResponse.file required")
    return out
