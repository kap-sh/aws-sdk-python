"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationReviewNotificationRecipient``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation_review_notification_recipient_type
    import aws_sdk_connect.types.evaluation_review_notification_recipient_value


class EvaluationReviewNotificationRecipient(TypedDict):
    type: "aws_sdk_connect.types.evaluation_review_notification_recipient_type.EvaluationReviewNotificationRecipientType"
    """<p>The type of notification recipient.</p>"""
    value: "aws_sdk_connect.types.evaluation_review_notification_recipient_value.EvaluationReviewNotificationRecipientValue"
    """<p>The value associated with the notification recipient type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationReviewNotificationRecipient) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.evaluation_review_notification_recipient_type

    out["Type"] = (
        aws_sdk_connect.types.evaluation_review_notification_recipient_type.serialize_json(
            value["type"]
        )
    )
    import aws_sdk_connect.types.evaluation_review_notification_recipient_value

    out["Value"] = (
        aws_sdk_connect.types.evaluation_review_notification_recipient_value.serialize_json(
            value["value"]
        )
    )
    return out


def deserialize_json(data: dict) -> EvaluationReviewNotificationRecipient:
    out: EvaluationReviewNotificationRecipient = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_connect.types.evaluation_review_notification_recipient_type

        out["type"] = (
            aws_sdk_connect.types.evaluation_review_notification_recipient_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        raise DeserializationError(
            "EvaluationReviewNotificationRecipient.type required"
        )
    if "Value" in data:
        import aws_sdk_connect.types.evaluation_review_notification_recipient_value

        out["value"] = (
            aws_sdk_connect.types.evaluation_review_notification_recipient_value.deserialize_json(
                data["Value"]
            )
        )
    else:
        raise DeserializationError(
            "EvaluationReviewNotificationRecipient.value required"
        )
    return out
