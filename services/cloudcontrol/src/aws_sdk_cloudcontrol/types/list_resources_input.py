"""Generated from Smithy shape ``com.amazonaws.cloudcontrol#ListResourcesInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudcontrol.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudcontrol.types.handler_next_token
    import aws_sdk_cloudcontrol.types.max_results
    import aws_sdk_cloudcontrol.types.properties
    import aws_sdk_cloudcontrol.types.role_arn
    import aws_sdk_cloudcontrol.types.type_name
    import aws_sdk_cloudcontrol.types.type_version_id


class ListResourcesInput(TypedDict):
    type_name: "aws_sdk_cloudcontrol.types.type_name.TypeName"
    """<p>The name of the resource type.</p>"""
    type_version_id: NotRequired[
        "aws_sdk_cloudcontrol.types.type_version_id.TypeVersionId"
    ]
    """<p>For private resource types, the type version to use in this resource operation. If you do not specify a resource version, CloudFormation uses the default version.</p>"""
    role_arn: NotRequired["aws_sdk_cloudcontrol.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role for Cloud Control API to use when performing this resource operation. The role specified must have the permissions required for this operation. The necessary permissions for each event handler are defined in the <code> <a href=\"https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html#schema-properties-handlers\">handlers</a> </code> section of the <a href=\"https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html\">resource type definition schema</a>.</p> <p>If you do not specify a role, Cloud Control API uses a temporary session created using your Amazon Web Services user credentials.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations.html#resource-operations-permissions\">Specifying credentials</a> in the <i>Amazon Web Services Cloud Control API User Guide</i>.</p>"""
    next_token: NotRequired[
        "aws_sdk_cloudcontrol.types.handler_next_token.HandlerNextToken"
    ]
    """<p>If the previous paginated request didn't return all of the remaining results, the response object's <code>NextToken</code> parameter value is set to a token. To retrieve the next set of results, call this action again and assign that token to the request object's <code>NextToken</code> parameter. If there are no remaining results, the previous response object's <code>NextToken</code> parameter is set to <code>null</code>.</p>"""
    max_results: NotRequired["aws_sdk_cloudcontrol.types.max_results.MaxResults"]
    """<p>Reserved.</p>"""
    resource_model: NotRequired["aws_sdk_cloudcontrol.types.properties.Properties"]
    """<p>The resource model to use to select the resources to return.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListResourcesInput) -> dict:
    out: dict = {}
    out["TypeName"] = value["type_name"]
    if "type_version_id" in value:
        out["TypeVersionId"] = value["type_version_id"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "resource_model" in value:
        out["ResourceModel"] = value["resource_model"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListResourcesInput:
    out: ListResourcesInput = {}  # type: ignore[typeddict-item]
    if "TypeName" in data:
        out["type_name"] = data["TypeName"]
    else:
        raise DeserializationError("ListResourcesInput.type_name required")
    if "TypeVersionId" in data:
        out["type_version_id"] = data["TypeVersionId"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "ResourceModel" in data:
        out["resource_model"] = data["ResourceModel"]
    return out
