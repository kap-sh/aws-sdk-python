"""Generated from Smithy shape ``com.amazonaws.ssm#ReviewInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.date_time
    import capo_ssm.types.review_status
    import capo_ssm.types.reviewer


class ReviewInformation(TypedDict, closed=True):
    reviewed_time: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The time that the reviewer took action on the document review request.</p>"""
    status: NotRequired["capo_ssm.types.review_status.ReviewStatus"]
    """<p>The current status of the document review request.</p>"""
    reviewer: NotRequired["capo_ssm.types.reviewer.Reviewer"]
    """<p>The reviewer assigned to take action on the document review request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReviewInformation) -> dict:
    out: dict = {}
    if "reviewed_time" in value:
        import capo_ssm.types.date_time

        out["ReviewedTime"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["reviewed_time"]
        )
    if "status" in value:
        import capo_ssm.types.review_status

        out["Status"] = capo_ssm.types.review_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "reviewer" in value:
        out["Reviewer"] = value["reviewer"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ReviewInformation:
    out: ReviewInformation = {}  # type: ignore[typeddict-item]
    if "ReviewedTime" in data:
        import capo_ssm.types.date_time

        out["reviewed_time"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["ReviewedTime"]
        )
    if "Status" in data:
        import capo_ssm.types.review_status

        out["status"] = capo_ssm.types.review_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "Reviewer" in data:
        out["reviewer"] = data["Reviewer"]
    return out
