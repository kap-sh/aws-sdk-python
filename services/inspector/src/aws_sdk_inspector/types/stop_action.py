"""Generated from Smithy shape ``com.amazonaws.inspector#StopAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector.errors import DeserializationError

StopAction: TypeAlias = Literal[
    "START_EVALUATION",
    "SKIP_EVALUATION",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "START_EVALUATION",
        "SKIP_EVALUATION",
    )
)


def serialize_aws_json_1_1(value: StopAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StopAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StopAction value: {data!r}")
    return cast(StopAction, data)
