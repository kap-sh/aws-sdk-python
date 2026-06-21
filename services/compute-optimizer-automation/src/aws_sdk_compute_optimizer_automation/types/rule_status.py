"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#RuleStatus``."""

from typing import Literal, TypeAlias, cast

RuleStatus: TypeAlias = Literal[
    "Active",
    "Inactive",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RuleStatus:
    return cast(RuleStatus, data)
