"""Generated from Smithy shape ``com.amazonaws.route53resolver#ResolverAutodefinedReverseStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route53resolver.errors import DeserializationError

ResolverAutodefinedReverseStatus: TypeAlias = Literal[
    "ENABLING",
    "ENABLED",
    "DISABLING",
    "DISABLED",
    "UPDATING_TO_USE_LOCAL_RESOURCE_SETTING",
    "USE_LOCAL_RESOURCE_SETTING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLING",
        "ENABLED",
        "DISABLING",
        "DISABLED",
        "UPDATING_TO_USE_LOCAL_RESOURCE_SETTING",
        "USE_LOCAL_RESOURCE_SETTING",
    )
)


def serialize_aws_json_1_1(value: ResolverAutodefinedReverseStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResolverAutodefinedReverseStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ResolverAutodefinedReverseStatus value: {data!r}"
        )
    return cast(ResolverAutodefinedReverseStatus, data)
