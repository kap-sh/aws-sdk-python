"""Generated from Smithy shape ``com.amazonaws.connect#ActionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

ActionType: TypeAlias = Literal[
    "CREATE_TASK",
    "ASSIGN_CONTACT_CATEGORY",
    "GENERATE_EVENTBRIDGE_EVENT",
    "SEND_NOTIFICATION",
    "CREATE_CASE",
    "UPDATE_CASE",
    "ASSIGN_SLA",
    "END_ASSOCIATED_TASKS",
    "SUBMIT_AUTO_EVALUATION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATE_TASK",
        "ASSIGN_CONTACT_CATEGORY",
        "GENERATE_EVENTBRIDGE_EVENT",
        "SEND_NOTIFICATION",
        "CREATE_CASE",
        "UPDATE_CASE",
        "ASSIGN_SLA",
        "END_ASSOCIATED_TASKS",
        "SUBMIT_AUTO_EVALUATION",
    )
)


def serialize_json(value: ActionType) -> str:
    return value


def deserialize_json(data: str) -> ActionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ActionType value: {data!r}")
    return cast(ActionType, data)
