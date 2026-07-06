"""Generated from Smithy shape ``com.amazonaws.wafv2#GetIPSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.entity_id
    import aws_sdk_wafv2.types.entity_name
    import aws_sdk_wafv2.types.scope


class GetIPSetRequest(TypedDict, closed=True):
    name: "aws_sdk_wafv2.types.entity_name.EntityName"
    """<p>The name of the IP set. You cannot change the name of an <code>IPSet</code> after you create it.</p>"""
    scope: "aws_sdk_wafv2.types.scope.Scope"
    """<p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>"""
    id: "aws_sdk_wafv2.types.entity_id.EntityId"
    """<p>A unique identifier for the set. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetIPSetRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_wafv2.types.scope

    out["Scope"] = aws_sdk_wafv2.types.scope.serialize_aws_json_1_1(value["scope"])
    out["Id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetIPSetRequest:
    out: GetIPSetRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("GetIPSetRequest.name required")
    if "Scope" in data:
        import aws_sdk_wafv2.types.scope

        out["scope"] = aws_sdk_wafv2.types.scope.deserialize_aws_json_1_1(data["Scope"])
    else:
        raise DeserializationError("GetIPSetRequest.scope required")
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("GetIPSetRequest.id required")
    return out
