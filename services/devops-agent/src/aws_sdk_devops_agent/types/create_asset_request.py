"""Generated from Smithy shape ``com.amazonaws.devopsagent#CreateAssetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.agent_space_id
    import aws_sdk_devops_agent.types.asset_content
    import aws_sdk_devops_agent.types.asset_type


class CreateAssetRequest(TypedDict, closed=True):
    agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier for the agent space where the asset will be created</p>"""
    asset_type: "aws_sdk_devops_agent.types.asset_type.AssetType"
    """<p>The type of asset to create</p>"""
    metadata: NotRequired["object"]
    """<p>The metadata describing this asset</p>"""
    content: "aws_sdk_devops_agent.types.asset_content.AssetContent"
    """<p>The content for the asset. Provide a single file or a zip bundle.</p>"""
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier used for idempotent asset creation</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAssetRequest) -> dict:
    out: dict = {}
    out["assetType"] = value["asset_type"]
    if "metadata" in value:
        out["metadata"] = value["metadata"]
    import aws_sdk_devops_agent.types.asset_content

    out["content"] = aws_sdk_devops_agent.types.asset_content.serialize_json(
        value["content"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateAssetRequest:
    out: CreateAssetRequest = {}  # type: ignore[typeddict-item]
    if "assetType" in data:
        out["asset_type"] = data["assetType"]
    else:
        raise DeserializationError("CreateAssetRequest.asset_type required")
    if "metadata" in data:
        out["metadata"] = data["metadata"]
    if "content" in data:
        import aws_sdk_devops_agent.types.asset_content

        out["content"] = aws_sdk_devops_agent.types.asset_content.deserialize_json(
            data["content"]
        )
    else:
        raise DeserializationError("CreateAssetRequest.content required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
