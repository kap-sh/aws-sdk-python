"""Generated from Smithy shape ``com.amazonaws.lightsail#AttachLoadBalancerTlsCertificateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.resource_name


class AttachLoadBalancerTlsCertificateRequest(TypedDict):
    load_balancer_name: "aws_sdk_lightsail.types.resource_name.ResourceName"
    """<p>The name of the load balancer to which you want to associate the SSL/TLS certificate.</p>"""
    certificate_name: "aws_sdk_lightsail.types.resource_name.ResourceName"
    """<p>The name of your SSL/TLS certificate.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttachLoadBalancerTlsCertificateRequest) -> dict:
    out: dict = {}
    out["loadBalancerName"] = value["load_balancer_name"]
    out["certificateName"] = value["certificate_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AttachLoadBalancerTlsCertificateRequest:
    out: AttachLoadBalancerTlsCertificateRequest = {}  # type: ignore[typeddict-item]
    if "loadBalancerName" in data:
        out["load_balancer_name"] = data["loadBalancerName"]
    else:
        raise DeserializationError(
            "AttachLoadBalancerTlsCertificateRequest.load_balancer_name required"
        )
    if "certificateName" in data:
        out["certificate_name"] = data["certificateName"]
    else:
        raise DeserializationError(
            "AttachLoadBalancerTlsCertificateRequest.certificate_name required"
        )
    return out
