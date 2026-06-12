"""Generated from Smithy shape ``com.amazonaws.budgets#NotificationState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_budgets.errors import DeserializationError

NotificationState: TypeAlias = Literal[
    "OK",
    "ALARM",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OK",
        "ALARM",
    )
)


def serialize_aws_json_1_1(value: NotificationState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NotificationState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NotificationState value: {data!r}")
    return cast(NotificationState, data)
