"""Generated from Smithy shape ``com.amazonaws.route53resolver#ResolverEndpointStatus``."""

from typing import Literal, TypeAlias, cast

ResolverEndpointStatus: TypeAlias = Literal[
    "CREATING",
    "OPERATIONAL",
    "UPDATING",
    "AUTO_RECOVERING",
    "ACTION_NEEDED",
    "DELETING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResolverEndpointStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResolverEndpointStatus:
    return cast(ResolverEndpointStatus, data)
