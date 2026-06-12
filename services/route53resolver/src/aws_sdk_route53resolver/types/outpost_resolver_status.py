"""Generated from Smithy shape ``com.amazonaws.route53resolver#OutpostResolverStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route53resolver.errors import DeserializationError

OutpostResolverStatus: TypeAlias = Literal[
    "CREATING",
    "OPERATIONAL",
    "UPDATING",
    "DELETING",
    "ACTION_NEEDED",
    "FAILED_CREATION",
    "FAILED_DELETION",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "OPERATIONAL",
        "UPDATING",
        "DELETING",
        "ACTION_NEEDED",
        "FAILED_CREATION",
        "FAILED_DELETION",
    )
)


def serialize_aws_json_1_1(value: OutpostResolverStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OutpostResolverStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OutpostResolverStatus value: {data!r}")
    return cast(OutpostResolverStatus, data)
