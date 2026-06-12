"""Generated from Smithy shape ``com.amazonaws.route53resolver#ResolverEndpointDirection``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route53resolver.errors import DeserializationError

ResolverEndpointDirection: TypeAlias = Literal[
    "INBOUND",
    "OUTBOUND",
    "INBOUND_DELEGATION",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INBOUND",
        "OUTBOUND",
        "INBOUND_DELEGATION",
    )
)


def serialize_aws_json_1_1(value: ResolverEndpointDirection) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResolverEndpointDirection:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResolverEndpointDirection value: {data!r}")
    return cast(ResolverEndpointDirection, data)
