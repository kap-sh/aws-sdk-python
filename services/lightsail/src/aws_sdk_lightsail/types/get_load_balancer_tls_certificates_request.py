"""Generated from Smithy shape ``com.amazonaws.lightsail#GetLoadBalancerTlsCertificatesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.resource_name


class GetLoadBalancerTlsCertificatesRequest(TypedDict, closed=True):
    load_balancer_name: "aws_sdk_lightsail.types.resource_name.ResourceName"
    """<p>The name of the load balancer you associated with your SSL/TLS certificate.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLoadBalancerTlsCertificatesRequest) -> dict:
    out: dict = {}
    out["loadBalancerName"] = value["load_balancer_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLoadBalancerTlsCertificatesRequest:
    out: GetLoadBalancerTlsCertificatesRequest = {}  # type: ignore[typeddict-item]
    if "loadBalancerName" in data:
        out["load_balancer_name"] = data["loadBalancerName"]
    else:
        raise DeserializationError(
            "GetLoadBalancerTlsCertificatesRequest.load_balancer_name required"
        )
    return out
