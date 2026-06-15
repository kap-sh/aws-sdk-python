"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdateWorkloadIdentityRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.resource_oauth2_return_url_list_type
    import aws_sdk_bedrock_agentcore_control.types.workload_identity_name_type


class UpdateWorkloadIdentityRequest(TypedDict):
    name: "aws_sdk_bedrock_agentcore_control.types.workload_identity_name_type.WorkloadIdentityNameType"
    """<p>The name of the workload identity to update.</p>"""
    allowed_resource_oauth2_return_urls: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.resource_oauth2_return_url_list_type.ResourceOauth2ReturnUrlListType"
    ]
    """<p>The new list of allowed OAuth2 return URLs for resources associated with this workload identity. This list replaces the existing list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWorkloadIdentityRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "allowed_resource_oauth2_return_urls" in value:
        import aws_sdk_bedrock_agentcore_control.types.resource_oauth2_return_url_list_type

        out["allowedResourceOauth2ReturnUrls"] = (
            aws_sdk_bedrock_agentcore_control.types.resource_oauth2_return_url_list_type.serialize_json(
                value["allowed_resource_oauth2_return_urls"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateWorkloadIdentityRequest:
    out: UpdateWorkloadIdentityRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateWorkloadIdentityRequest.name required")
    if "allowedResourceOauth2ReturnUrls" in data:
        import aws_sdk_bedrock_agentcore_control.types.resource_oauth2_return_url_list_type

        out["allowed_resource_oauth2_return_urls"] = (
            aws_sdk_bedrock_agentcore_control.types.resource_oauth2_return_url_list_type.deserialize_json(
                data["allowedResourceOauth2ReturnUrls"]
            )
        )
    return out
