"""Generated from Smithy shape ``com.amazonaws.lightsail#LoadBalancerProtocol``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

LoadBalancerProtocol: TypeAlias = Literal[
    "HTTP_HTTPS",
    "HTTP",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HTTP_HTTPS",
        "HTTP",
    )
)


def serialize_aws_json_1_1(value: LoadBalancerProtocol) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LoadBalancerProtocol:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LoadBalancerProtocol value: {data!r}")
    return cast(LoadBalancerProtocol, data)
