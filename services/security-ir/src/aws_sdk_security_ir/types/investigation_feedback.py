"""Generated from Smithy shape ``com.amazonaws.securityir#InvestigationFeedback``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_security_ir.types.feedback_comment
    import aws_sdk_security_ir.types.usefulness_rating


class InvestigationFeedback(TypedDict):
    usefulness: NotRequired[
        "aws_sdk_security_ir.types.usefulness_rating.UsefulnessRating"
    ]
    """<p>User assessment of the investigation result's quality and helpfulness. This rating indicates how valuable the investigation findings were in addressing the case.</p>"""
    comment: NotRequired["aws_sdk_security_ir.types.feedback_comment.FeedbackComment"]
    """<p>Optional user comments providing additional context about the investigation feedback. This allows users to explain their rating or provide suggestions for improvement.</p>"""
    submitted_at: NotRequired["datetime.datetime"]
    """<p>ISO 8601 timestamp when the feedback was submitted. This records when the user provided their assessment of the investigation results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvestigationFeedback) -> dict:
    out: dict = {}
    if "usefulness" in value:
        import aws_sdk_security_ir.types.usefulness_rating

        out["usefulness"] = aws_sdk_security_ir.types.usefulness_rating.serialize_json(
            value["usefulness"]
        )
    if "comment" in value:
        out["comment"] = value["comment"]
    if "submitted_at" in value:
        import aws_sdk_security_ir.types._prelude.timestamp

        out["submittedAt"] = (
            aws_sdk_security_ir.types._prelude.timestamp.serialize_json(
                value["submitted_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> InvestigationFeedback:
    out: InvestigationFeedback = {}  # type: ignore[typeddict-item]
    if "usefulness" in data:
        import aws_sdk_security_ir.types.usefulness_rating

        out["usefulness"] = (
            aws_sdk_security_ir.types.usefulness_rating.deserialize_json(
                data["usefulness"]
            )
        )
    if "comment" in data:
        out["comment"] = data["comment"]
    if "submittedAt" in data:
        import aws_sdk_security_ir.types._prelude.timestamp

        out["submitted_at"] = (
            aws_sdk_security_ir.types._prelude.timestamp.deserialize_json(
                data["submittedAt"]
            )
        )
    return out
