"""Generated from Smithy shape ``com.amazonaws.frauddetector#DetectorVersionStatus``."""

from typing import Literal, TypeAlias, cast

DetectorVersionStatus: TypeAlias = Literal[
    "DRAFT",
    "ACTIVE",
    "INACTIVE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectorVersionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DetectorVersionStatus:
    return cast(DetectorVersionStatus, data)
