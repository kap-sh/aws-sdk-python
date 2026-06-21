"""Generated from Smithy shape ``com.amazonaws.mturk#QualificationTypeStatus``."""

from typing import Literal, TypeAlias, cast

QualificationTypeStatus: TypeAlias = Literal[
    "Active",
    "Inactive",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QualificationTypeStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> QualificationTypeStatus:
    return cast(QualificationTypeStatus, data)
