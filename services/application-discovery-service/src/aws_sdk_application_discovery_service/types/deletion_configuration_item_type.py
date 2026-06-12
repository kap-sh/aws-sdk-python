"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#DeletionConfigurationItemType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_application_discovery_service.errors import DeserializationError

DeletionConfigurationItemType: TypeAlias = Literal["SERVER",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("SERVER",))


def serialize_aws_json_1_1(value: DeletionConfigurationItemType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeletionConfigurationItemType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DeletionConfigurationItemType value: {data!r}"
        )
    return cast(DeletionConfigurationItemType, data)
