"""Generated from Smithy shape ``com.amazonaws.lightsail#DeleteLoadBalancerTlsCertificateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.boolean
    import aws_sdk_lightsail.types.resource_name


class DeleteLoadBalancerTlsCertificateRequest(TypedDict):
    load_balancer_name: "aws_sdk_lightsail.types.resource_name.ResourceName"
    """<p>The load balancer name.</p>"""
    certificate_name: "aws_sdk_lightsail.types.resource_name.ResourceName"
    """<p>The SSL/TLS certificate name.</p>"""
    force: NotRequired["aws_sdk_lightsail.types.boolean.boolean"]
    """<p>When <code>true</code>, forces the deletion of an SSL/TLS certificate.</p> <p>There can be two certificates associated with a Lightsail load balancer: the primary and the backup. The <code>force</code> parameter is required when the primary SSL/TLS certificate is in use by an instance attached to the load balancer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteLoadBalancerTlsCertificateRequest) -> dict:
    out: dict = {}
    out["loadBalancerName"] = value["load_balancer_name"]
    out["certificateName"] = value["certificate_name"]
    if "force" in value:
        out["force"] = value["force"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteLoadBalancerTlsCertificateRequest:
    out: DeleteLoadBalancerTlsCertificateRequest = {}  # type: ignore[typeddict-item]
    if "loadBalancerName" in data:
        out["load_balancer_name"] = data["loadBalancerName"]
    else:
        raise DeserializationError(
            "DeleteLoadBalancerTlsCertificateRequest.load_balancer_name required"
        )
    if "certificateName" in data:
        out["certificate_name"] = data["certificateName"]
    else:
        raise DeserializationError(
            "DeleteLoadBalancerTlsCertificateRequest.certificate_name required"
        )
    if "force" in data:
        out["force"] = data["force"]
    return out
