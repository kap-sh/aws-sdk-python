"""Generated from Smithy shape ``com.amazonaws.wafv2#GetWebACLRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.entity_id
    import aws_sdk_wafv2.types.entity_name
    import aws_sdk_wafv2.types.resource_arn
    import aws_sdk_wafv2.types.scope


class GetWebACLRequest(TypedDict, closed=True):
    name: NotRequired["aws_sdk_wafv2.types.entity_name.EntityName"]
    """<p>The name of the web ACL. You cannot change the name of a web ACL after you create it.</p>"""
    scope: NotRequired["aws_sdk_wafv2.types.scope.Scope"]
    """<p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>"""
    id: NotRequired["aws_sdk_wafv2.types.entity_id.EntityId"]
    """<p>The unique identifier for the web ACL. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.</p>"""
    arn: NotRequired["aws_sdk_wafv2.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the web ACL that you want to retrieve. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetWebACLRequest) -> dict:
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


def deserialize_aws_json_1_1(data: dict) -> GetWebACLRequest:
    out: GetWebACLRequest = {}  # type: ignore[typeddict-item]
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
