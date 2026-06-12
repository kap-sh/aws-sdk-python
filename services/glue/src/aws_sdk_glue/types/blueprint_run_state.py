"""Generated from Smithy shape ``com.amazonaws.glue#BlueprintRunState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

BlueprintRunState: TypeAlias = Literal[
    "RUNNING",
    "SUCCEEDED",
    "FAILED",
    "ROLLING_BACK",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RUNNING",
        "SUCCEEDED",
        "FAILED",
        "ROLLING_BACK",
    )
)


def serialize_aws_json_1_1(value: BlueprintRunState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BlueprintRunState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BlueprintRunState value: {data!r}")
    return cast(BlueprintRunState, data)
