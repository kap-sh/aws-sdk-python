"""Generated from Smithy shape ``com.amazonaws.sagemaker#DetailedModelPackageStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

DetailedModelPackageStatus: TypeAlias = Literal[
    "NotStarted",
    "InProgress",
    "Completed",
    "Failed",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NotStarted",
        "InProgress",
        "Completed",
        "Failed",
    )
)


def serialize_aws_json_1_1(value: DetailedModelPackageStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DetailedModelPackageStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DetailedModelPackageStatus value: {data!r}"
        )
    return cast(DetailedModelPackageStatus, data)
