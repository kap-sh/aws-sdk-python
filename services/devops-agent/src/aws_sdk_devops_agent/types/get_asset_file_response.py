"""Generated from Smithy shape ``com.amazonaws.devopsagent#GetAssetFileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.asset_file


class GetAssetFileResponse(TypedDict, closed=True):
    file: "aws_sdk_devops_agent.types.asset_file.AssetFile"
    """<p>The asset file object</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAssetFileResponse) -> dict:
    out: dict = {}
    import aws_sdk_devops_agent.types.asset_file

    out["file"] = aws_sdk_devops_agent.types.asset_file.serialize_json(value["file"])
    return out


def deserialize_json(data: dict) -> GetAssetFileResponse:
    out: GetAssetFileResponse = {}  # type: ignore[typeddict-item]
    if "file" in data:
        import aws_sdk_devops_agent.types.asset_file

        out["file"] = aws_sdk_devops_agent.types.asset_file.deserialize_json(
            data["file"]
        )
    else:
        raise DeserializationError("GetAssetFileResponse.file required")
    return out
