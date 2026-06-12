"""Generated from Smithy shape ``com.amazonaws.sagemaker#SplitType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

SplitType: TypeAlias = Literal[
    "None",
    "Line",
    "RecordIO",
    "TFRecord",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "None",
        "Line",
        "RecordIO",
        "TFRecord",
    )
)


def serialize_aws_json_1_1(value: SplitType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SplitType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SplitType value: {data!r}")
    return cast(SplitType, data)
