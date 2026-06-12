"""Generated from Smithy shape ``com.amazonaws.configservice#OrganizationConfigRuleTriggerTypeNoSN``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_config_service.errors import DeserializationError

OrganizationConfigRuleTriggerTypeNoSN: TypeAlias = Literal[
    "ConfigurationItemChangeNotification",
    "OversizedConfigurationItemChangeNotification",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ConfigurationItemChangeNotification",
        "OversizedConfigurationItemChangeNotification",
    )
)


def serialize_aws_json_1_1(value: OrganizationConfigRuleTriggerTypeNoSN) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OrganizationConfigRuleTriggerTypeNoSN:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown OrganizationConfigRuleTriggerTypeNoSN value: {data!r}"
        )
    return cast(OrganizationConfigRuleTriggerTypeNoSN, data)
