"""Generated from Smithy shape ``com.amazonaws.glue#AdditionalOptionKeys``."""

from typing import Literal, TypeAlias, cast

AdditionalOptionKeys: TypeAlias = Literal[
    "performanceTuning.caching",
    "observations.scope",
    "compositeRuleEvaluation.method",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdditionalOptionKeys) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AdditionalOptionKeys:
    return cast(AdditionalOptionKeys, data)
