"""Generated from Smithy shape ``com.amazonaws.budgets#DeleteNotificationResponse``."""

from typing_extensions import TypedDict


class DeleteNotificationResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteNotificationResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteNotificationResponse:
    out: DeleteNotificationResponse = {}  # type: ignore[typeddict-item]
    return out
