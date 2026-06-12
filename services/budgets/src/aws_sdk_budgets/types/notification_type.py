"""Generated from Smithy shape ``com.amazonaws.budgets#NotificationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_budgets.errors import DeserializationError

"""<p> The type of a notification. It must be ACTUAL or FORECASTED.</p>"""
NotificationType: TypeAlias = Literal[
    "ACTUAL",
    "FORECASTED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTUAL",
        "FORECASTED",
    )
)


def serialize_aws_json_1_1(value: NotificationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NotificationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NotificationType value: {data!r}")
    return cast(NotificationType, data)
