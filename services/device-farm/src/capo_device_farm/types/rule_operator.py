"""Generated from Smithy shape ``com.amazonaws.devicefarm#RuleOperator``."""

from typing import Literal, TypeAlias, cast

RuleOperator: TypeAlias = Literal[
    "EQUALS",
    "LESS_THAN",
    "LESS_THAN_OR_EQUALS",
    "GREATER_THAN",
    "GREATER_THAN_OR_EQUALS",
    "IN",
    "NOT_IN",
    "CONTAINS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleOperator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RuleOperator:
    return cast(RuleOperator, data)
