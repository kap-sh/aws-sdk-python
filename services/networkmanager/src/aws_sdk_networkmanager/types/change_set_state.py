"""Generated from Smithy shape ``com.amazonaws.networkmanager#ChangeSetState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_networkmanager.errors import DeserializationError

ChangeSetState: TypeAlias = Literal[
    "PENDING_GENERATION",
    "FAILED_GENERATION",
    "READY_TO_EXECUTE",
    "EXECUTING",
    "EXECUTION_SUCCEEDED",
    "OUT_OF_DATE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING_GENERATION",
        "FAILED_GENERATION",
        "READY_TO_EXECUTE",
        "EXECUTING",
        "EXECUTION_SUCCEEDED",
        "OUT_OF_DATE",
    )
)


def serialize_json(value: ChangeSetState) -> str:
    return value


def deserialize_json(data: str) -> ChangeSetState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChangeSetState value: {data!r}")
    return cast(ChangeSetState, data)
