"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationReviewNotificationRecipientType``."""

from typing import Literal, TypeAlias, cast

EvaluationReviewNotificationRecipientType: TypeAlias = Literal["USER_ID",]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationReviewNotificationRecipientType) -> str:
    return value


def deserialize_json(data: str) -> EvaluationReviewNotificationRecipientType:
    return cast(EvaluationReviewNotificationRecipientType, data)
