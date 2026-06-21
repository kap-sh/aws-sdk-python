"""Generated from Smithy shape ``com.amazonaws.sagemaker#JoinSource``."""

from typing import Literal, TypeAlias, cast

JoinSource: TypeAlias = Literal[
    "Input",
    "None",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JoinSource) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> JoinSource:
    return cast(JoinSource, data)
