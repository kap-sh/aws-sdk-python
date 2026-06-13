"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateWorkloadIdentityResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.resource_oauth2_return_url_list_type
    import aws_sdk_bedrock_agentcore_control.types.workload_identity_arn_type
    import aws_sdk_bedrock_agentcore_control.types.workload_identity_name_type

class CreateWorkloadIdentityResponse(TypedDict):
    name: "aws_sdk_bedrock_agentcore_control.types.workload_identity_name_type.WorkloadIdentityNameType"
    """<p>The name of the workload identity.</p>"""
    workload_identity_arn: "aws_sdk_bedrock_agentcore_control.types.workload_identity_arn_type.WorkloadIdentityArnType"
    """<p>The Amazon Resource Name (ARN) of the workload identity.</p>"""
    allowed_resource_oauth2_return_urls: NotRequired["aws_sdk_bedrock_agentcore_control.types.resource_oauth2_return_url_list_type.ResourceOauth2ReturnUrlListType"]
    """<p>The list of allowed OAuth2 return URLs for resources associated with this workload identity.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkloadIdentityResponse) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["workloadIdentityArn"] = value["workload_identity_arn"]
    if "allowed_resource_oauth2_return_urls" in value:
        import aws_sdk_bedrock_agentcore_control.types.resource_oauth2_return_url_list_type
        out["allowedResourceOauth2ReturnUrls"] = aws_sdk_bedrock_agentcore_control.types.resource_oauth2_return_url_list_type.serialize_json(value["allowed_resource_oauth2_return_urls"])
    return out


def deserialize_json(data: dict) -> CreateWorkloadIdentityResponse:
    out: CreateWorkloadIdentityResponse = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateWorkloadIdentityResponse.name required")
    if "workloadIdentityArn" in data:
        out["workload_identity_arn"] = data["workloadIdentityArn"]
    else:
        raise DeserializationError("CreateWorkloadIdentityResponse.workload_identity_arn required")
    if "allowedResourceOauth2ReturnUrls" in data:
        import aws_sdk_bedrock_agentcore_control.types.resource_oauth2_return_url_list_type
        out["allowed_resource_oauth2_return_urls"] = aws_sdk_bedrock_agentcore_control.types.resource_oauth2_return_url_list_type.deserialize_json(data["allowedResourceOauth2ReturnUrls"])
    return out