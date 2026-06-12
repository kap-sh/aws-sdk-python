"""Generated from Smithy shape ``com.amazonaws.configservice#OrganizationConfigRuleTriggerType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_config_service.errors import DeserializationError

OrganizationConfigRuleTriggerType: TypeAlias = Literal[
    "ConfigurationItemChangeNotification",
    "OversizedConfigurationItemChangeNotification",
    "ScheduledNotification",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ConfigurationItemChangeNotification",
        "OversizedConfigurationItemChangeNotification",
        "ScheduledNotification",
    )
)


def serialize_aws_json_1_1(value: OrganizationConfigRuleTriggerType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OrganizationConfigRuleTriggerType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown OrganizationConfigRuleTriggerType value: {data!r}"
        )
    return cast(OrganizationConfigRuleTriggerType, data)
