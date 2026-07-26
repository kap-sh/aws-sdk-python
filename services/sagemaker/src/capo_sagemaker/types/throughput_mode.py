"""Generated from Smithy shape ``com.amazonaws.sagemaker#ThroughputMode``."""

from typing import Literal, TypeAlias, cast

ThroughputMode: TypeAlias = Literal[
    "OnDemand",
    "Provisioned",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ThroughputMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ThroughputMode:
    return cast(ThroughputMode, data)
