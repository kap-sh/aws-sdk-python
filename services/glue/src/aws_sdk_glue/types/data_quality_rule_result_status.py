"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityRuleResultStatus``."""

from typing import Literal, TypeAlias, cast

DataQualityRuleResultStatus: TypeAlias = Literal[
    "PASS",
    "FAIL",
    "ERROR",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityRuleResultStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataQualityRuleResultStatus:
    return cast(DataQualityRuleResultStatus, data)
