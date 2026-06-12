"""Generated from Smithy shape ``com.amazonaws.applicationinsights#DiscoveryType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_application_insights.errors import DeserializationError

DiscoveryType: TypeAlias = Literal[
    "RESOURCE_GROUP_BASED",
    "ACCOUNT_BASED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RESOURCE_GROUP_BASED",
        "ACCOUNT_BASED",
    )
)


def serialize_aws_json_1_1(value: DiscoveryType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DiscoveryType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DiscoveryType value: {data!r}")
    return cast(DiscoveryType, data)
