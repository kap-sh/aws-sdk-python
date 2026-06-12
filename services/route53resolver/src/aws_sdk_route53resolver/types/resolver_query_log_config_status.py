"""Generated from Smithy shape ``com.amazonaws.route53resolver#ResolverQueryLogConfigStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route53resolver.errors import DeserializationError

ResolverQueryLogConfigStatus: TypeAlias = Literal[
    "CREATING",
    "CREATED",
    "DELETING",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "CREATED",
        "DELETING",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: ResolverQueryLogConfigStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResolverQueryLogConfigStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ResolverQueryLogConfigStatus value: {data!r}"
        )
    return cast(ResolverQueryLogConfigStatus, data)
