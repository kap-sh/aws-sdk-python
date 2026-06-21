"""Generated from Smithy shape ``com.amazonaws.glue#JobMode``."""

from typing import Literal, TypeAlias, cast

JobMode: TypeAlias = Literal[
    "SCRIPT",
    "VISUAL",
    "NOTEBOOK",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> JobMode:
    return cast(JobMode, data)
