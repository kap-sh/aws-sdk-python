"""Generated from Smithy shape ``com.amazonaws.budgets#NotificationType``."""

from typing import Literal, TypeAlias, cast

"""<p> The type of a notification. It must be ACTUAL or FORECASTED.</p>"""
NotificationType: TypeAlias = Literal[
    "ACTUAL",
    "FORECASTED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotificationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NotificationType:
    return cast(NotificationType, data)
