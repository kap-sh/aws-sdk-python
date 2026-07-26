"""Generated from Smithy shape ``com.amazonaws.apprunner#OperationType``."""

from typing import Literal, TypeAlias, cast

OperationType: TypeAlias = Literal[
    "START_DEPLOYMENT",
    "CREATE_SERVICE",
    "PAUSE_SERVICE",
    "RESUME_SERVICE",
    "DELETE_SERVICE",
    "UPDATE_SERVICE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OperationType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> OperationType:
    return cast(OperationType, data)
