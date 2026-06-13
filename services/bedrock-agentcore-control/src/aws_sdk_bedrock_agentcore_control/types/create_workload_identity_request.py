"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateWorkloadIdentityRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.resource_oauth2_return_url_list_type
    import aws_sdk_bedrock_agentcore_control.types.tags_map
    import aws_sdk_bedrock_agentcore_control.types.workload_identity_name_type

class CreateWorkloadIdentityRequest(TypedDict):
    name: "aws_sdk_bedrock_agentcore_control.types.workload_identity_name_type.WorkloadIdentityNameType"
    """<p>The name of the workload identity. The name must be unique within your account.</p>"""
    allowed_resource_oauth2_return_urls: NotRequired["aws_sdk_bedrock_agentcore_control.types.resource_oauth2_return_url_list_type.ResourceOauth2ReturnUrlListType"]
    """<p>The list of allowed OAuth2 return URLs for resources associated with this workload identity.</p>"""
    tags: NotRequired["aws_sdk_bedrock_agentcore_control.types.tags_map.TagsMap"]
    """<p>A map of tag keys and values to assign to the workload identity. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkloadIdentityRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "allowed_resource_oauth2_return_urls" in value:
        import aws_sdk_bedrock_agentcore_control.types.resource_oauth2_return_url_list_type
        out["allowedResourceOauth2ReturnUrls"] = aws_sdk_bedrock_agentcore_control.types.resource_oauth2_return_url_list_type.serialize_json(value["allowed_resource_oauth2_return_urls"])
    if "tags" in value:
        import aws_sdk_bedrock_agentcore_control.types.tags_map
        out["tags"] = aws_sdk_bedrock_agentcore_control.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateWorkloadIdentityRequest:
    out: CreateWorkloadIdentityRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateWorkloadIdentityRequest.name required")
    if "allowedResourceOauth2ReturnUrls" in data:
        import aws_sdk_bedrock_agentcore_control.types.resource_oauth2_return_url_list_type
        out["allowed_resource_oauth2_return_urls"] = aws_sdk_bedrock_agentcore_control.types.resource_oauth2_return_url_list_type.deserialize_json(data["allowedResourceOauth2ReturnUrls"])
    if "tags" in data:
        import aws_sdk_bedrock_agentcore_control.types.tags_map
        out["tags"] = aws_sdk_bedrock_agentcore_control.types.tags_map.deserialize_json(data["tags"])
    return out