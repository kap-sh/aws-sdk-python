"""Generated from Smithy shape ``com.amazonaws.securityir#SendFeedbackRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_security_ir.errors import DeserializationError

if TYPE_CHECKING:
    import capo_security_ir.types.case_id
    import capo_security_ir.types.feedback_comment
    import capo_security_ir.types.result_id
    import capo_security_ir.types.usefulness_rating


class SendFeedbackRequest(TypedDict, closed=True):
    case_id: "capo_security_ir.types.case_id.CaseId"
    """<p>Send feedback based on request caseID</p>"""
    result_id: "capo_security_ir.types.result_id.ResultId"
    """<p>Send feedback based on request result ID</p>"""
    usefulness: "capo_security_ir.types.usefulness_rating.UsefulnessRating"
    """<p>Required enum value indicating user assessment of result q.....</p>"""
    comment: NotRequired["capo_security_ir.types.feedback_comment.FeedbackComment"]
    """<p>Send feedback based on request comments</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendFeedbackRequest) -> dict:
    out: dict = {}
    import capo_security_ir.types.usefulness_rating

    out["usefulness"] = capo_security_ir.types.usefulness_rating.serialize_json(
        value["usefulness"]
    )
    if "comment" in value:
        out["comment"] = value["comment"]
    return out


def deserialize_json(data: dict) -> SendFeedbackRequest:
    out: SendFeedbackRequest = {}  # type: ignore[typeddict-item]
    if "usefulness" in data:
        import capo_security_ir.types.usefulness_rating

        out["usefulness"] = capo_security_ir.types.usefulness_rating.deserialize_json(
            data["usefulness"]
        )
    else:
        raise DeserializationError("SendFeedbackRequest.usefulness required")
    if "comment" in data:
        out["comment"] = data["comment"]
    return out
