"""Generated from Smithy shape ``com.amazonaws.lightsail#GetLoadBalancerTlsPoliciesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.load_balancer_tls_policy_list
    import aws_sdk_lightsail.types.string


class GetLoadBalancerTlsPoliciesResult(TypedDict):
    tls_policies: NotRequired[
        "aws_sdk_lightsail.types.load_balancer_tls_policy_list.LoadBalancerTlsPolicyList"
    ]
    """<p>An array of objects that describe the TLS security policies that are available.</p>"""
    next_page_token: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The token to advance to the next page of results from your request.</p> <p>A next page token is not returned if there are no more results to display.</p> <p>To get the next page of results, perform another <code>GetLoadBalancerTlsPolicies</code> request and specify the next page token using the <code>pageToken</code> parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLoadBalancerTlsPoliciesResult) -> dict:
    out: dict = {}
    if "tls_policies" in value:
        import aws_sdk_lightsail.types.load_balancer_tls_policy_list

        out["tlsPolicies"] = (
            aws_sdk_lightsail.types.load_balancer_tls_policy_list.serialize_aws_json_1_1(
                value["tls_policies"]
            )
        )
    if "next_page_token" in value:
        out["nextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLoadBalancerTlsPoliciesResult:
    out: GetLoadBalancerTlsPoliciesResult = {}  # type: ignore[typeddict-item]
    if "tlsPolicies" in data:
        import aws_sdk_lightsail.types.load_balancer_tls_policy_list

        out["tls_policies"] = (
            aws_sdk_lightsail.types.load_balancer_tls_policy_list.deserialize_aws_json_1_1(
                data["tlsPolicies"]
            )
        )
    if "nextPageToken" in data:
        out["next_page_token"] = data["nextPageToken"]
    return out
