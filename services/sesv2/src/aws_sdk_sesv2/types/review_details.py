"""Generated from Smithy shape ``com.amazonaws.sesv2#ReviewDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.case_id
    import aws_sdk_sesv2.types.review_status


class ReviewDetails(TypedDict):
    status: NotRequired["aws_sdk_sesv2.types.review_status.ReviewStatus"]
    """<p>The status of the latest review of your account. The status can be one of the following:</p> <ul> <li> <p> <code>PENDING</code> – We have received your appeal and are in the process of reviewing it.</p> </li> <li> <p> <code>GRANTED</code> – Your appeal has been reviewed and your production access has been granted.</p> </li> <li> <p> <code>DENIED</code> – Your appeal has been reviewed and your production access has been denied.</p> </li> <li> <p> <code>FAILED</code> – An internal error occurred and we didn't receive your appeal. You can submit your appeal again.</p> </li> </ul>"""
    case_id: NotRequired["aws_sdk_sesv2.types.case_id.CaseId"]
    """<p>The associated support center case ID (if any).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReviewDetails) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_sesv2.types.review_status

        out["Status"] = aws_sdk_sesv2.types.review_status.serialize_json(
            value["status"]
        )
    if "case_id" in value:
        out["CaseId"] = value["case_id"]
    return out


def deserialize_json(data: dict) -> ReviewDetails:
    out: ReviewDetails = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_sesv2.types.review_status

        out["status"] = aws_sdk_sesv2.types.review_status.deserialize_json(
            data["Status"]
        )
    if "CaseId" in data:
        out["case_id"] = data["CaseId"]
    return out
