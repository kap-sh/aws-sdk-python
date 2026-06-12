"""Generated from Smithy shape ``com.amazonaws.ssm#SessionState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

SessionState: TypeAlias = Literal[
    "Active",
    "History",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Active",
        "History",
    )
)


def serialize_aws_json_1_1(value: SessionState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SessionState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SessionState value: {data!r}")
    return cast(SessionState, data)
