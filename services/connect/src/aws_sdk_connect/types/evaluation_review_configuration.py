"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationReviewConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation_review_notification_recipient_list
    import aws_sdk_connect.types.integer


class EvaluationReviewConfiguration(TypedDict):
    review_notification_recipients: "aws_sdk_connect.types.evaluation_review_notification_recipient_list.EvaluationReviewNotificationRecipientList"
    """<p>List of recipients who should be notified when a review is requested.</p>"""
    eligibility_days: "aws_sdk_connect.types.integer.Integer"
    """<p>Number of days during which a request for review can be submitted for evaluations created from this form.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationReviewConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.evaluation_review_notification_recipient_list

    out["ReviewNotificationRecipients"] = (
        aws_sdk_connect.types.evaluation_review_notification_recipient_list.serialize_json(
            value["review_notification_recipients"]
        )
    )
    out["EligibilityDays"] = value.get("eligibility_days", 0)
    return out


def deserialize_json(data: dict) -> EvaluationReviewConfiguration:
    out: EvaluationReviewConfiguration = {}  # type: ignore[typeddict-item]
    if "ReviewNotificationRecipients" in data:
        import aws_sdk_connect.types.evaluation_review_notification_recipient_list

        out["review_notification_recipients"] = (
            aws_sdk_connect.types.evaluation_review_notification_recipient_list.deserialize_json(
                data["ReviewNotificationRecipients"]
            )
        )
    else:
        raise DeserializationError(
            "EvaluationReviewConfiguration.review_notification_recipients required"
        )
    if "EligibilityDays" in data:
        out["eligibility_days"] = data["EligibilityDays"]
    else:
        out["eligibility_days"] = 0
    return out
