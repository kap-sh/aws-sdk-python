"""Generated from Smithy shape ``com.amazonaws.wafv2#Body``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.oversize_handling


class Body(TypedDict, closed=True):
    oversize_handling: NotRequired[
        "capo_wafv2.types.oversize_handling.OversizeHandling"
    ]
    """<p>What WAF should do if the body is larger than WAF can inspect. </p> <p>WAF does not support inspecting the entire contents of the web request body if the body exceeds the limit for the resource type. When a web request body is larger than the limit, the underlying host service only forwards the contents that are within the limit to WAF for inspection. </p> <ul> <li> <p>For Application Load Balancer and AppSync, the limit is fixed at 8 KB (8,192 bytes).</p> </li> <li> <p>For CloudFront, API Gateway, Amazon Cognito, App Runner, and Verified Access, the default limit is 16 KB (16,384 bytes), and you can increase the limit for each resource type in the web ACL <code>AssociationConfig</code>, for additional processing fees. </p> </li> <li> <p>For Amplify, use the CloudFront limit.</p> </li> </ul> <p>The options for oversize handling are the following:</p> <ul> <li> <p> <code>CONTINUE</code> - Inspect the available body contents normally, according to the rule inspection criteria. </p> </li> <li> <p> <code>MATCH</code> - Treat the web request as matching the rule statement. WAF applies the rule action to the request.</p> </li> <li> <p> <code>NO_MATCH</code> - Treat the web request as not matching the rule statement.</p> </li> </ul> <p>You can combine the <code>MATCH</code> or <code>NO_MATCH</code> settings for oversize handling with your rule and web ACL action settings, so that you block any request whose body is over the limit. </p> <p>Default: <code>CONTINUE</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Body) -> dict:
    out: dict = {}
    if "oversize_handling" in value:
        import capo_wafv2.types.oversize_handling

        out["OversizeHandling"] = (
            capo_wafv2.types.oversize_handling.serialize_aws_json_1_1(
                value["oversize_handling"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Body:
    out: Body = {}  # type: ignore[typeddict-item]
    if "OversizeHandling" in data:
        import capo_wafv2.types.oversize_handling

        out["oversize_handling"] = (
            capo_wafv2.types.oversize_handling.deserialize_aws_json_1_1(
                data["OversizeHandling"]
            )
        )
    return out
