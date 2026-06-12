"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#ConfigurationItemType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_application_discovery_service.errors import DeserializationError

ConfigurationItemType: TypeAlias = Literal[
    "SERVER",
    "PROCESS",
    "CONNECTION",
    "APPLICATION",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SERVER",
        "PROCESS",
        "CONNECTION",
        "APPLICATION",
    )
)


def serialize_aws_json_1_1(value: ConfigurationItemType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConfigurationItemType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConfigurationItemType value: {data!r}")
    return cast(ConfigurationItemType, data)
