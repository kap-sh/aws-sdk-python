"""Generated from Smithy shape ``com.amazonaws.eventbridge#RuleState``."""

from typing import Literal, TypeAlias, cast

RuleState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
    "ENABLED_WITH_ALL_CLOUDTRAIL_MANAGEMENT_EVENTS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RuleState:
    return cast(RuleState, data)
