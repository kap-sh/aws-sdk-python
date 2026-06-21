"""Generated from Smithy shape ``com.amazonaws.configservice#ConfigRuleState``."""

from typing import Literal, TypeAlias, cast

ConfigRuleState: TypeAlias = Literal[
    "ACTIVE",
    "DELETING",
    "DELETING_RESULTS",
    "EVALUATING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigRuleState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConfigRuleState:
    return cast(ConfigRuleState, data)
