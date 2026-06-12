"""Generated from Smithy shape ``com.amazonaws.sagemaker#FailureHandlingPolicy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

FailureHandlingPolicy: TypeAlias = Literal[
    "ROLLBACK_ON_FAILURE",
    "DO_NOTHING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ROLLBACK_ON_FAILURE",
        "DO_NOTHING",
    )
)


def serialize_aws_json_1_1(value: FailureHandlingPolicy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FailureHandlingPolicy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FailureHandlingPolicy value: {data!r}")
    return cast(FailureHandlingPolicy, data)
