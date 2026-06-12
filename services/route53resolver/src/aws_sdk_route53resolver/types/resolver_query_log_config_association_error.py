"""Generated from Smithy shape ``com.amazonaws.route53resolver#ResolverQueryLogConfigAssociationError``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route53resolver.errors import DeserializationError

ResolverQueryLogConfigAssociationError: TypeAlias = Literal[
    "NONE",
    "DESTINATION_NOT_FOUND",
    "ACCESS_DENIED",
    "INTERNAL_SERVICE_ERROR",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "DESTINATION_NOT_FOUND",
        "ACCESS_DENIED",
        "INTERNAL_SERVICE_ERROR",
    )
)


def serialize_aws_json_1_1(value: ResolverQueryLogConfigAssociationError) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResolverQueryLogConfigAssociationError:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ResolverQueryLogConfigAssociationError value: {data!r}"
        )
    return cast(ResolverQueryLogConfigAssociationError, data)
