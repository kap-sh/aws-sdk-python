"""Generated from Smithy shape ``com.amazonaws.configservice#OrganizationConfigRuleTriggerType``."""

from typing import Literal, TypeAlias, cast

OrganizationConfigRuleTriggerType: TypeAlias = Literal[
    "ConfigurationItemChangeNotification",
    "OversizedConfigurationItemChangeNotification",
    "ScheduledNotification",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationConfigRuleTriggerType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OrganizationConfigRuleTriggerType:
    return cast(OrganizationConfigRuleTriggerType, data)
