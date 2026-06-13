"""Generated from Smithy shape ``com.amazonaws.devopsagent#UpdateAssetFileResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.asset_file


class UpdateAssetFileResponse(TypedDict):
    file: "aws_sdk_devops_agent.types.asset_file.AssetFile"
    """<p>The asset file object</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAssetFileResponse) -> dict:
    out: dict = {}
    import aws_sdk_devops_agent.types.asset_file

    out["file"] = aws_sdk_devops_agent.types.asset_file.serialize_json(value["file"])
    return out


def deserialize_json(data: dict) -> UpdateAssetFileResponse:
    out: UpdateAssetFileResponse = {}  # type: ignore[typeddict-item]
    if "file" in data:
        import aws_sdk_devops_agent.types.asset_file

        out["file"] = aws_sdk_devops_agent.types.asset_file.deserialize_json(
            data["file"]
        )
    else:
        raise DeserializationError("UpdateAssetFileResponse.file required")
    return out
