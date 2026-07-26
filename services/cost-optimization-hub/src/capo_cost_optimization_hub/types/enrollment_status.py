"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#EnrollmentStatus``."""

from typing import Literal, TypeAlias, cast

EnrollmentStatus: TypeAlias = Literal[
    "Active",
    "Inactive",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EnrollmentStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EnrollmentStatus:
    return cast(EnrollmentStatus, data)
