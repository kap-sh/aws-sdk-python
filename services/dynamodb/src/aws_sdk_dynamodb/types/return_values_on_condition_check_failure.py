"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReturnValuesOnConditionCheckFailure``."""

from typing import Literal, TypeAlias, cast

ReturnValuesOnConditionCheckFailure: TypeAlias = Literal[
    "ALL_OLD",
    "NONE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReturnValuesOnConditionCheckFailure) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ReturnValuesOnConditionCheckFailure:
    return cast(ReturnValuesOnConditionCheckFailure, data)
