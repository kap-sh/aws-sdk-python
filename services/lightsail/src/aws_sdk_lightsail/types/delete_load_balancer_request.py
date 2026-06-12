"""Generated from Smithy shape ``com.amazonaws.lightsail#DeleteLoadBalancerRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.resource_name


class DeleteLoadBalancerRequest(TypedDict):
    load_balancer_name: "aws_sdk_lightsail.types.resource_name.ResourceName"
    """<p>The name of the load balancer you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteLoadBalancerRequest) -> dict:
    out: dict = {}
    out["loadBalancerName"] = value["load_balancer_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteLoadBalancerRequest:
    out: DeleteLoadBalancerRequest = {}  # type: ignore[typeddict-item]
    if "loadBalancerName" in data:
        out["load_balancer_name"] = data["loadBalancerName"]
    else:
        raise DeserializationError(
            "DeleteLoadBalancerRequest.load_balancer_name required"
        )
    return out
