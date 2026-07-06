"""Generated from Smithy shape ``com.amazonaws.lightsail#GetLoadBalancerResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.load_balancer


class GetLoadBalancerResult(TypedDict, closed=True):
    load_balancer: NotRequired["aws_sdk_lightsail.types.load_balancer.LoadBalancer"]
    """<p>An object containing information about your load balancer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLoadBalancerResult) -> dict:
    out: dict = {}
    if "load_balancer" in value:
        import aws_sdk_lightsail.types.load_balancer

        out["loadBalancer"] = (
            aws_sdk_lightsail.types.load_balancer.serialize_aws_json_1_1(
                value["load_balancer"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLoadBalancerResult:
    out: GetLoadBalancerResult = {}  # type: ignore[typeddict-item]
    if "loadBalancer" in data:
        import aws_sdk_lightsail.types.load_balancer

        out["load_balancer"] = (
            aws_sdk_lightsail.types.load_balancer.deserialize_aws_json_1_1(
                data["loadBalancer"]
            )
        )
    return out
