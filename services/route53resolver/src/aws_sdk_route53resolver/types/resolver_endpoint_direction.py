"""Generated from Smithy shape ``com.amazonaws.route53resolver#ResolverEndpointDirection``."""

from typing import Literal, TypeAlias, cast

ResolverEndpointDirection: TypeAlias = Literal[
    "INBOUND",
    "OUTBOUND",
    "INBOUND_DELEGATION",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResolverEndpointDirection) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResolverEndpointDirection:
    return cast(ResolverEndpointDirection, data)
