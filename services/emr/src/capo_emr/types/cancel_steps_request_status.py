"""Generated from Smithy shape ``com.amazonaws.emr#CancelStepsRequestStatus``."""

from typing import Literal, TypeAlias, cast

CancelStepsRequestStatus: TypeAlias = Literal[
    "SUBMITTED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelStepsRequestStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CancelStepsRequestStatus:
    return cast(CancelStepsRequestStatus, data)
