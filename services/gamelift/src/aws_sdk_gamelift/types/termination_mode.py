"""Generated from Smithy shape ``com.amazonaws.gamelift#TerminationMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

TerminationMode: TypeAlias = Literal[
    "TRIGGER_ON_PROCESS_TERMINATE",
    "FORCE_TERMINATE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TRIGGER_ON_PROCESS_TERMINATE",
        "FORCE_TERMINATE",
    )
)


def serialize_aws_json_1_1(value: TerminationMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TerminationMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TerminationMode value: {data!r}")
    return cast(TerminationMode, data)
