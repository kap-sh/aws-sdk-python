"""Generated from Smithy shape ``com.amazonaws.frauddetector#TrainingDataSourceEnum``."""

from typing import Literal, TypeAlias, cast

TrainingDataSourceEnum: TypeAlias = Literal[
    "EXTERNAL_EVENTS",
    "INGESTED_EVENTS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrainingDataSourceEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TrainingDataSourceEnum:
    return cast(TrainingDataSourceEnum, data)
