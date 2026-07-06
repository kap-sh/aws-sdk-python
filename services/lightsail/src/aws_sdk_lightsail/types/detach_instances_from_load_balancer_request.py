"""Generated from Smithy shape ``com.amazonaws.lightsail#DetachInstancesFromLoadBalancerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.resource_name
    import aws_sdk_lightsail.types.resource_name_list


class DetachInstancesFromLoadBalancerRequest(TypedDict, closed=True):
    load_balancer_name: "aws_sdk_lightsail.types.resource_name.ResourceName"
    """<p>The name of the Lightsail load balancer.</p>"""
    instance_names: "aws_sdk_lightsail.types.resource_name_list.ResourceNameList"
    """<p>An array of strings containing the names of the instances you want to detach from the load balancer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetachInstancesFromLoadBalancerRequest) -> dict:
    out: dict = {}
    out["loadBalancerName"] = value["load_balancer_name"]
    import aws_sdk_lightsail.types.resource_name_list

    out["instanceNames"] = (
        aws_sdk_lightsail.types.resource_name_list.serialize_aws_json_1_1(
            value["instance_names"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DetachInstancesFromLoadBalancerRequest:
    out: DetachInstancesFromLoadBalancerRequest = {}  # type: ignore[typeddict-item]
    if "loadBalancerName" in data:
        out["load_balancer_name"] = data["loadBalancerName"]
    else:
        raise DeserializationError(
            "DetachInstancesFromLoadBalancerRequest.load_balancer_name required"
        )
    if "instanceNames" in data:
        import aws_sdk_lightsail.types.resource_name_list

        out["instance_names"] = (
            aws_sdk_lightsail.types.resource_name_list.deserialize_aws_json_1_1(
                data["instanceNames"]
            )
        )
    else:
        raise DeserializationError(
            "DetachInstancesFromLoadBalancerRequest.instance_names required"
        )
    return out
