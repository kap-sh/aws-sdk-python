"""Generated from Smithy shape ``com.amazonaws.ssm#RebootOption``."""

from typing import Literal, TypeAlias, cast

RebootOption: TypeAlias = Literal[
    "RebootIfNeeded",
    "NoReboot",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RebootOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RebootOption:
    return cast(RebootOption, data)
