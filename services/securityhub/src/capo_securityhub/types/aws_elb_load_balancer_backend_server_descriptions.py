"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsElbLoadBalancerBackendServerDescriptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_elb_load_balancer_backend_server_description

AwsElbLoadBalancerBackendServerDescriptions: TypeAlias = list[
    "capo_securityhub.types.aws_elb_load_balancer_backend_server_description.AwsElbLoadBalancerBackendServerDescription"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsElbLoadBalancerBackendServerDescriptions) -> list:
    import capo_securityhub.types.aws_elb_load_balancer_backend_server_description

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_elb_load_balancer_backend_server_description.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsElbLoadBalancerBackendServerDescriptions:
    import capo_securityhub.types.aws_elb_load_balancer_backend_server_description

    out: AwsElbLoadBalancerBackendServerDescriptions = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_elb_load_balancer_backend_server_description.deserialize_json(
                item
            )
        )
    return out
