"""Generated from Smithy shape ``com.amazonaws.emr#ProfilerType``."""

from typing import Literal, TypeAlias, cast

ProfilerType: TypeAlias = Literal[
    "SHS",
    "TEZUI",
    "YTS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProfilerType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProfilerType:
    return cast(ProfilerType, data)
