"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationReviewNotificationRecipientList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.evaluation_review_notification_recipient

EvaluationReviewNotificationRecipientList: TypeAlias = list[
    "capo_connect.types.evaluation_review_notification_recipient.EvaluationReviewNotificationRecipient"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationReviewNotificationRecipientList) -> list:
    import capo_connect.types.evaluation_review_notification_recipient

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.evaluation_review_notification_recipient.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> EvaluationReviewNotificationRecipientList:
    import capo_connect.types.evaluation_review_notification_recipient

    out: EvaluationReviewNotificationRecipientList = []
    for item in data:
        out.append(
            capo_connect.types.evaluation_review_notification_recipient.deserialize_json(
                item
            )
        )
    return out
