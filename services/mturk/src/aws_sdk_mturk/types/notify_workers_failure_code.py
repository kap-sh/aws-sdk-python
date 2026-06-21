"""Generated from Smithy shape ``com.amazonaws.mturk#NotifyWorkersFailureCode``."""

from typing import Literal, TypeAlias, cast

NotifyWorkersFailureCode: TypeAlias = Literal[
    "SoftFailure",
    "HardFailure",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotifyWorkersFailureCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NotifyWorkersFailureCode:
    return cast(NotifyWorkersFailureCode, data)
