"""Generated from Smithy shape ``com.amazonaws.sesv2#Complaint``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.complaint_feedback_type
    import aws_sdk_sesv2.types.complaint_sub_type


class Complaint(TypedDict):
    complaint_sub_type: NotRequired[
        "aws_sdk_sesv2.types.complaint_sub_type.ComplaintSubType"
    ]
    """<p> Can either be <code>null</code> or <code>OnAccountSuppressionList</code>. If the value is <code>OnAccountSuppressionList</code>, SES accepted the message, but didn't attempt to send it because it was on the account-level suppression list. </p>"""
    complaint_feedback_type: NotRequired[
        "aws_sdk_sesv2.types.complaint_feedback_type.ComplaintFeedbackType"
    ]
    """<p> The value of the <code>Feedback-Type</code> field from the feedback report received from the ISP. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Complaint) -> dict:
    out: dict = {}
    if "complaint_sub_type" in value:
        out["ComplaintSubType"] = value["complaint_sub_type"]
    if "complaint_feedback_type" in value:
        out["ComplaintFeedbackType"] = value["complaint_feedback_type"]
    return out


def deserialize_json(data: dict) -> Complaint:
    out: Complaint = {}  # type: ignore[typeddict-item]
    if "ComplaintSubType" in data:
        out["complaint_sub_type"] = data["ComplaintSubType"]
    if "ComplaintFeedbackType" in data:
        out["complaint_feedback_type"] = data["ComplaintFeedbackType"]
    return out
