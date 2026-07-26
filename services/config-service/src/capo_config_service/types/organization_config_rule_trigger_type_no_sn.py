"""Generated from Smithy shape ``com.amazonaws.configservice#OrganizationConfigRuleTriggerTypeNoSN``."""

from typing import Literal, TypeAlias, cast

OrganizationConfigRuleTriggerTypeNoSN: TypeAlias = Literal[
    "ConfigurationItemChangeNotification",
    "OversizedConfigurationItemChangeNotification",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationConfigRuleTriggerTypeNoSN) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OrganizationConfigRuleTriggerTypeNoSN:
    return cast(OrganizationConfigRuleTriggerTypeNoSN, data)
