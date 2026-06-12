"""Generated from Smithy shape ``com.amazonaws.route53resolver#ResolverQueryLogConfigAssociationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route53resolver.errors import DeserializationError

ResolverQueryLogConfigAssociationStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "ACTION_NEEDED",
    "DELETING",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "ACTIVE",
        "ACTION_NEEDED",
        "DELETING",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: ResolverQueryLogConfigAssociationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResolverQueryLogConfigAssociationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ResolverQueryLogConfigAssociationStatus value: {data!r}"
        )
    return cast(ResolverQueryLogConfigAssociationStatus, data)
