"""Generated from Smithy shape ``com.amazonaws.codepipeline#Result``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codepipeline.errors import DeserializationError

Result: TypeAlias = Literal[
    "ROLLBACK",
    "FAIL",
    "RETRY",
    "SKIP",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ROLLBACK",
        "FAIL",
        "RETRY",
        "SKIP",
    )
)


def serialize_aws_json_1_1(value: Result) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Result:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Result value: {data!r}")
    return cast(Result, data)
