"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#LatestInferenceResult``."""

from typing import Literal, TypeAlias, cast

LatestInferenceResult: TypeAlias = Literal[
    "ANOMALOUS",
    "NORMAL",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LatestInferenceResult) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LatestInferenceResult:
    return cast(LatestInferenceResult, data)
