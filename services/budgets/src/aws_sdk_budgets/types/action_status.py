"""Generated from Smithy shape ``com.amazonaws.budgets#ActionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_budgets.errors import DeserializationError

ActionStatus: TypeAlias = Literal[
    "STANDBY",
    "PENDING",
    "EXECUTION_IN_PROGRESS",
    "EXECUTION_SUCCESS",
    "EXECUTION_FAILURE",
    "REVERSE_IN_PROGRESS",
    "REVERSE_SUCCESS",
    "REVERSE_FAILURE",
    "RESET_IN_PROGRESS",
    "RESET_FAILURE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STANDBY",
        "PENDING",
        "EXECUTION_IN_PROGRESS",
        "EXECUTION_SUCCESS",
        "EXECUTION_FAILURE",
        "REVERSE_IN_PROGRESS",
        "REVERSE_SUCCESS",
        "REVERSE_FAILURE",
        "RESET_IN_PROGRESS",
        "RESET_FAILURE",
    )
)


def serialize_aws_json_1_1(value: ActionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ActionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ActionStatus value: {data!r}")
    return cast(ActionStatus, data)
