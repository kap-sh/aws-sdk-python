"""Generated from Smithy shape ``com.amazonaws.timestreamquery#ScalarType``."""

from typing import Literal, TypeAlias, cast

ScalarType: TypeAlias = Literal[
    "VARCHAR",
    "BOOLEAN",
    "BIGINT",
    "DOUBLE",
    "TIMESTAMP",
    "DATE",
    "TIME",
    "INTERVAL_DAY_TO_SECOND",
    "INTERVAL_YEAR_TO_MONTH",
    "UNKNOWN",
    "INTEGER",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ScalarType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ScalarType:
    return cast(ScalarType, data)
