"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsElbLoadBalancerBackendServerDescriptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_elb_load_balancer_backend_server_description

AwsElbLoadBalancerBackendServerDescriptions: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_elb_load_balancer_backend_server_description.AwsElbLoadBalancerBackendServerDescription"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsElbLoadBalancerBackendServerDescriptions) -> list:
    import aws_sdk_securityhub.types.aws_elb_load_balancer_backend_server_description

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_elb_load_balancer_backend_server_description.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsElbLoadBalancerBackendServerDescriptions:
    import aws_sdk_securityhub.types.aws_elb_load_balancer_backend_server_description

    out: AwsElbLoadBalancerBackendServerDescriptions = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_elb_load_balancer_backend_server_description.deserialize_json(
                item
            )
        )
    return out
