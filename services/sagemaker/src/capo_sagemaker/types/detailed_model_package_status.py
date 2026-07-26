"""Generated from Smithy shape ``com.amazonaws.sagemaker#DetailedModelPackageStatus``."""

from typing import Literal, TypeAlias, cast

DetailedModelPackageStatus: TypeAlias = Literal[
    "NotStarted",
    "InProgress",
    "Completed",
    "Failed",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetailedModelPackageStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DetailedModelPackageStatus:
    return cast(DetailedModelPackageStatus, data)
