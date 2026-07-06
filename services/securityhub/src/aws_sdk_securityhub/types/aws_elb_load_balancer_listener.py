"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsElbLoadBalancerListener``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string


class AwsElbLoadBalancerListener(TypedDict, closed=True):
    instance_port: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The port on which the instance is listening.</p>"""
    instance_protocol: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The protocol to use to route traffic to instances.</p> <p>Valid values: <code>HTTP</code> | <code>HTTPS</code> | <code>TCP</code> | <code>SSL</code> </p>"""
    load_balancer_port: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The port on which the load balancer is listening.</p> <p>On EC2-VPC, you can specify any port from the range 1-65535.</p> <p>On EC2-Classic, you can specify any port from the following list: 25, 80, 443, 465, 587, 1024-65535.</p>"""
    protocol: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The load balancer transport protocol to use for routing.</p> <p>Valid values: <code>HTTP</code> | <code>HTTPS</code> | <code>TCP</code> | <code>SSL</code> </p>"""
    ssl_certificate_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the server certificate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsElbLoadBalancerListener) -> dict:
    out: dict = {}
    if "instance_port" in value:
        out["InstancePort"] = value["instance_port"]
    if "instance_protocol" in value:
        out["InstanceProtocol"] = value["instance_protocol"]
    if "load_balancer_port" in value:
        out["LoadBalancerPort"] = value["load_balancer_port"]
    if "protocol" in value:
        out["Protocol"] = value["protocol"]
    if "ssl_certificate_id" in value:
        out["SslCertificateId"] = value["ssl_certificate_id"]
    return out


def deserialize_json(data: dict) -> AwsElbLoadBalancerListener:
    out: AwsElbLoadBalancerListener = {}  # type: ignore[typeddict-item]
    if "InstancePort" in data:
        out["instance_port"] = data["InstancePort"]
    if "InstanceProtocol" in data:
        out["instance_protocol"] = data["InstanceProtocol"]
    if "LoadBalancerPort" in data:
        out["load_balancer_port"] = data["LoadBalancerPort"]
    if "Protocol" in data:
        out["protocol"] = data["Protocol"]
    if "SslCertificateId" in data:
        out["ssl_certificate_id"] = data["SslCertificateId"]
    return out
