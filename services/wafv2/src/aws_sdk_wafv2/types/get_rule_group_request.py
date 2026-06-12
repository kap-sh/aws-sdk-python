"""Generated from Smithy shape ``com.amazonaws.wafv2#GetRuleGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.entity_id
    import aws_sdk_wafv2.types.entity_name
    import aws_sdk_wafv2.types.resource_arn
    import aws_sdk_wafv2.types.scope


class GetRuleGroupRequest(TypedDict):
    name: NotRequired["aws_sdk_wafv2.types.entity_name.EntityName"]
    """<p>The name of the rule group. You cannot change the name of a rule group after you create it.</p>"""
    scope: NotRequired["aws_sdk_wafv2.types.scope.Scope"]
    """<p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>"""
    id: NotRequired["aws_sdk_wafv2.types.entity_id.EntityId"]
    """<p>A unique identifier for the rule group. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.</p>"""
    arn: NotRequired["aws_sdk_wafv2.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the entity.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRuleGroupRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "scope" in value:
        import aws_sdk_wafv2.types.scope

        out["Scope"] = aws_sdk_wafv2.types.scope.serialize_aws_json_1_1(value["scope"])
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["ARN"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRuleGroupRequest:
    out: GetRuleGroupRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Scope" in data:
        import aws_sdk_wafv2.types.scope

        out["scope"] = aws_sdk_wafv2.types.scope.deserialize_aws_json_1_1(data["Scope"])
    if "Id" in data:
        out["id"] = data["Id"]
    if "ARN" in data:
        out["arn"] = data["ARN"]
    return out
