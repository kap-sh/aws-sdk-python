"""Generated from Smithy shape ``com.amazonaws.sagemaker#RecordWrapper``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

RecordWrapper: TypeAlias = Literal[
    "None",
    "RecordIO",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "None",
        "RecordIO",
    )
)


def serialize_aws_json_1_1(value: RecordWrapper) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RecordWrapper:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecordWrapper value: {data!r}")
    return cast(RecordWrapper, data)
