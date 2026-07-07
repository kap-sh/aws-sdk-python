"""Generated from Smithy shape ``com.amazonaws.devopsagent#GetAssetContentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.asset_zip_content


class GetAssetContentResponse(TypedDict, closed=True):
    content: "aws_sdk_devops_agent.types.asset_zip_content.AssetZipContent"
    """<p>The asset content as a zip file</p>"""
    version: "int"
    """<p>The asset version this content belongs to</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAssetContentResponse) -> dict:
    out: dict = {}
    import aws_sdk_devops_agent.types.asset_zip_content

    out["content"] = aws_sdk_devops_agent.types.asset_zip_content.serialize_json(
        value["content"]
    )
    out["version"] = value["version"]
    return out


def deserialize_json(data: dict) -> GetAssetContentResponse:
    out: GetAssetContentResponse = {}  # type: ignore[typeddict-item]
    if "content" in data:
        import aws_sdk_devops_agent.types.asset_zip_content

        out["content"] = aws_sdk_devops_agent.types.asset_zip_content.deserialize_json(
            data["content"]
        )
    else:
        raise DeserializationError("GetAssetContentResponse.content required")
    if "version" in data:
        out["version"] = data["version"]
    else:
        raise DeserializationError("GetAssetContentResponse.version required")
    return out
