"""Generated from Smithy shape ``com.amazonaws.frauddetector#DataSource``."""

from typing import Literal, TypeAlias, cast

DataSource: TypeAlias = Literal[
    "EVENT",
    "MODEL_SCORE",
    "EXTERNAL_MODEL_SCORE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataSource) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataSource:
    return cast(DataSource, data)
