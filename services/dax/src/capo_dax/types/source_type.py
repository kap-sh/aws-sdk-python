"""Generated from Smithy shape ``com.amazonaws.dax#SourceType``."""

from typing import Literal, TypeAlias, cast

SourceType: TypeAlias = Literal[
    "CLUSTER",
    "PARAMETER_GROUP",
    "SUBNET_GROUP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SourceType:
    return cast(SourceType, data)
