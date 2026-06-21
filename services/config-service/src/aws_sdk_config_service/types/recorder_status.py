"""Generated from Smithy shape ``com.amazonaws.configservice#RecorderStatus``."""

from typing import Literal, TypeAlias, cast

RecorderStatus: TypeAlias = Literal[
    "Pending",
    "Success",
    "Failure",
    "NotApplicable",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecorderStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RecorderStatus:
    return cast(RecorderStatus, data)
