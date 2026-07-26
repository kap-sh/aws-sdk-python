"""Generated from Smithy shape ``com.amazonaws.lightsail#GetLoadBalancersResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.load_balancer_list
    import capo_lightsail.types.string


class GetLoadBalancersResult(TypedDict, closed=True):
    load_balancers: NotRequired[
        "capo_lightsail.types.load_balancer_list.LoadBalancerList"
    ]
    """<p>An array of LoadBalancer objects describing your load balancers.</p>"""
    next_page_token: NotRequired["capo_lightsail.types.string.string"]
    """<p>The token to advance to the next page of results from your request.</p> <p>A next page token is not returned if there are no more results to display.</p> <p>To get the next page of results, perform another <code>GetLoadBalancers</code> request and specify the next page token using the <code>pageToken</code> parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLoadBalancersResult) -> dict:
    out: dict = {}
    if "load_balancers" in value:
        import capo_lightsail.types.load_balancer_list

        out["loadBalancers"] = (
            capo_lightsail.types.load_balancer_list.serialize_aws_json_1_1(
                value["load_balancers"]
            )
        )
    if "next_page_token" in value:
        out["nextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLoadBalancersResult:
    out: GetLoadBalancersResult = {}  # type: ignore[typeddict-item]
    if "loadBalancers" in data:
        import capo_lightsail.types.load_balancer_list

        out["load_balancers"] = (
            capo_lightsail.types.load_balancer_list.deserialize_aws_json_1_1(
                data["loadBalancers"]
            )
        )
    if "nextPageToken" in data:
        out["next_page_token"] = data["nextPageToken"]
    return out
