"""Generated from Smithy shape ``com.amazonaws.wafv2#CheckCapacityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.rules
    import aws_sdk_wafv2.types.scope


class CheckCapacityRequest(TypedDict, closed=True):
    scope: "aws_sdk_wafv2.types.scope.Scope"
    """<p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>"""
    rules: "aws_sdk_wafv2.types.rules.Rules"
    """<p>An array of <a>Rule</a> that you're configuring to use in a rule group or web ACL. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CheckCapacityRequest) -> dict:
    out: dict = {}
    import aws_sdk_wafv2.types.scope

    out["Scope"] = aws_sdk_wafv2.types.scope.serialize_aws_json_1_1(value["scope"])
    import aws_sdk_wafv2.types.rules

    out["Rules"] = aws_sdk_wafv2.types.rules.serialize_aws_json_1_1(value["rules"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CheckCapacityRequest:
    out: CheckCapacityRequest = {}  # type: ignore[typeddict-item]
    if "Scope" in data:
        import aws_sdk_wafv2.types.scope

        out["scope"] = aws_sdk_wafv2.types.scope.deserialize_aws_json_1_1(data["Scope"])
    else:
        raise DeserializationError("CheckCapacityRequest.scope required")
    if "Rules" in data:
        import aws_sdk_wafv2.types.rules

        out["rules"] = aws_sdk_wafv2.types.rules.deserialize_aws_json_1_1(data["Rules"])
    else:
        raise DeserializationError("CheckCapacityRequest.rules required")
    return out
