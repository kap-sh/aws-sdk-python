"""Generated from Smithy shape ``com.amazonaws.sagemaker#FlatInvocations``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

FlatInvocations: TypeAlias = Literal[
    "Continue",
    "Stop",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Continue",
        "Stop",
    )
)


def serialize_aws_json_1_1(value: FlatInvocations) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FlatInvocations:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FlatInvocations value: {data!r}")
    return cast(FlatInvocations, data)
