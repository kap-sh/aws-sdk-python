"""Generated from Smithy shape ``com.amazonaws.codepipeline#StageRetryMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codepipeline.errors import DeserializationError

StageRetryMode: TypeAlias = Literal[
    "FAILED_ACTIONS",
    "ALL_ACTIONS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FAILED_ACTIONS",
        "ALL_ACTIONS",
    )
)


def serialize_aws_json_1_1(value: StageRetryMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StageRetryMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StageRetryMode value: {data!r}")
    return cast(StageRetryMode, data)
