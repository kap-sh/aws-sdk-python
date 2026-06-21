"""Generated from Smithy shape ``com.amazonaws.route53resolver#ResolverEndpointType``."""

from typing import Literal, TypeAlias, cast

ResolverEndpointType: TypeAlias = Literal[
    "IPV6",
    "IPV4",
    "DUALSTACK",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResolverEndpointType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResolverEndpointType:
    return cast(ResolverEndpointType, data)
