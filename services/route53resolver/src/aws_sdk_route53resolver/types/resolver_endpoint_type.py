"""Generated from Smithy shape ``com.amazonaws.route53resolver#ResolverEndpointType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route53resolver.errors import DeserializationError

ResolverEndpointType: TypeAlias = Literal[
    "IPV6",
    "IPV4",
    "DUALSTACK",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IPV6",
        "IPV4",
        "DUALSTACK",
    )
)


def serialize_aws_json_1_1(value: ResolverEndpointType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResolverEndpointType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResolverEndpointType value: {data!r}")
    return cast(ResolverEndpointType, data)
