"""Generated from Smithy shape ``com.amazonaws.route53resolver#ResolverEndpointStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route53resolver.errors import DeserializationError

ResolverEndpointStatus: TypeAlias = Literal[
    "CREATING",
    "OPERATIONAL",
    "UPDATING",
    "AUTO_RECOVERING",
    "ACTION_NEEDED",
    "DELETING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "OPERATIONAL",
        "UPDATING",
        "AUTO_RECOVERING",
        "ACTION_NEEDED",
        "DELETING",
    )
)


def serialize_aws_json_1_1(value: ResolverEndpointStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResolverEndpointStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResolverEndpointStatus value: {data!r}")
    return cast(ResolverEndpointStatus, data)
