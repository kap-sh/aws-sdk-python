"""Generated from Smithy shape ``com.amazonaws.emr#ReconfigurationType``."""

from typing import Literal, TypeAlias, cast

ReconfigurationType: TypeAlias = Literal[
    "OVERWRITE",
    "MERGE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReconfigurationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReconfigurationType:
    return cast(ReconfigurationType, data)
