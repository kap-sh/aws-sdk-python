"""Generated from Smithy shape ``com.amazonaws.codepipeline#RetryTrigger``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codepipeline.errors import DeserializationError

RetryTrigger: TypeAlias = Literal[
    "AutomatedStageRetry",
    "ManualStageRetry",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AutomatedStageRetry",
        "ManualStageRetry",
    )
)


def serialize_aws_json_1_1(value: RetryTrigger) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RetryTrigger:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RetryTrigger value: {data!r}")
    return cast(RetryTrigger, data)
