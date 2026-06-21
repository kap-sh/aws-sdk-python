"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#RuntimeEnvironment``."""

from typing import Literal, TypeAlias, cast

RuntimeEnvironment: TypeAlias = Literal[
    "SQL-1_0",
    "FLINK-1_6",
    "FLINK-1_8",
    "ZEPPELIN-FLINK-1_0",
    "FLINK-1_11",
    "FLINK-1_13",
    "ZEPPELIN-FLINK-2_0",
    "FLINK-1_15",
    "ZEPPELIN-FLINK-3_0",
    "FLINK-1_18",
    "FLINK-1_19",
    "FLINK-1_20",
    "FLINK-2_2",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuntimeEnvironment) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RuntimeEnvironment:
    return cast(RuntimeEnvironment, data)
