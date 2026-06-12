"""Generated from Smithy shape ``com.amazonaws.athena#WorkGroupState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_athena.errors import DeserializationError

WorkGroupState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_aws_json_1_1(value: WorkGroupState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WorkGroupState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WorkGroupState value: {data!r}")
    return cast(WorkGroupState, data)
