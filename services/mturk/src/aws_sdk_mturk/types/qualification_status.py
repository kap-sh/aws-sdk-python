"""Generated from Smithy shape ``com.amazonaws.mturk#QualificationStatus``."""

from typing import Literal, TypeAlias, cast

QualificationStatus: TypeAlias = Literal[
    "Granted",
    "Revoked",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QualificationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> QualificationStatus:
    return cast(QualificationStatus, data)
