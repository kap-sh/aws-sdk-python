"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#DbStorageType``."""

from typing import Literal, TypeAlias, cast

DbStorageType: TypeAlias = Literal[
    "InfluxIOIncludedT1",
    "InfluxIOIncludedT2",
    "InfluxIOIncludedT3",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DbStorageType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DbStorageType:
    return cast(DbStorageType, data)
