"""Generated from Smithy shape ``com.amazonaws.lightsail#LoadBalancerProtocol``."""

from typing import Literal, TypeAlias, cast

LoadBalancerProtocol: TypeAlias = Literal[
    "HTTP_HTTPS",
    "HTTP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LoadBalancerProtocol) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LoadBalancerProtocol:
    return cast(LoadBalancerProtocol, data)
