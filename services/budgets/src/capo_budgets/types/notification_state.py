"""Generated from Smithy shape ``com.amazonaws.budgets#NotificationState``."""

from typing import Literal, TypeAlias, cast

NotificationState: TypeAlias = Literal[
    "OK",
    "ALARM",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotificationState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NotificationState:
    return cast(NotificationState, data)
