"""Generated from Smithy shape ``com.amazonaws.route53resolver#ResolverDNSSECValidationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route53resolver.errors import DeserializationError

ResolverDNSSECValidationStatus: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: ResolverDNSSECValidationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResolverDNSSECValidationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ResolverDNSSECValidationStatus value: {data!r}"
        )
    return cast(ResolverDNSSECValidationStatus, data)
