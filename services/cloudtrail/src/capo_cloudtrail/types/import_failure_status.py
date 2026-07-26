"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ImportFailureStatus``."""

from typing import Literal, TypeAlias, cast

ImportFailureStatus: TypeAlias = Literal[
    "FAILED",
    "RETRY",
    "SUCCEEDED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportFailureStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImportFailureStatus:
    return cast(ImportFailureStatus, data)
