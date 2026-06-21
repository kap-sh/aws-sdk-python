"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#OriginTypeValue``."""

from typing import Literal, TypeAlias, cast

OriginTypeValue: TypeAlias = Literal[
    "SOURCE",
    "TARGET",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OriginTypeValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OriginTypeValue:
    return cast(OriginTypeValue, data)
