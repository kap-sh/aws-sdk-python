"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationReviewMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.evaluation_review_request_comment_list
    import aws_sdk_connect.types.resource_id
    import aws_sdk_connect.types.timestamp


class EvaluationReviewMetadata(TypedDict):
    review_id: NotRequired["aws_sdk_connect.types.resource_id.ResourceId"]
    """<p>The unique identifier for the evaluation review.</p>"""
    requested_time: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when the evaluation review was requested.</p>"""
    requested_by: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The user who requested the evaluation review.</p>"""
    created_time: "aws_sdk_connect.types.timestamp.Timestamp"
    """<p>The timestamp when the evaluation review was created.</p>"""
    created_by: "aws_sdk_connect.types.arn.ARN"
    """<p>The user who created the evaluation review.</p>"""
    review_request_comments: "aws_sdk_connect.types.evaluation_review_request_comment_list.EvaluationReviewRequestCommentList"
    """<p>Comments provided when requesting the evaluation review.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationReviewMetadata) -> dict:
    out: dict = {}
    if "review_id" in value:
        out["ReviewId"] = value["review_id"]
    if "requested_time" in value:
        import aws_sdk_connect.types.timestamp

        out["RequestedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["requested_time"]
        )
    if "requested_by" in value:
        out["RequestedBy"] = value["requested_by"]
    import datetime

    import aws_sdk_connect.types.timestamp

    out["CreatedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
        value.get(
            "created_time", datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
        )
    )
    out["CreatedBy"] = value.get("created_by", "n/a")
    import aws_sdk_connect.types.evaluation_review_request_comment_list

    out["ReviewRequestComments"] = (
        aws_sdk_connect.types.evaluation_review_request_comment_list.serialize_json(
            value["review_request_comments"]
        )
    )
    return out


def deserialize_json(data: dict) -> EvaluationReviewMetadata:
    out: EvaluationReviewMetadata = {}  # type: ignore[typeddict-item]
    if "ReviewId" in data:
        out["review_id"] = data["ReviewId"]
    if "RequestedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["requested_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["RequestedTime"]
        )
    if "RequestedBy" in data:
        out["requested_by"] = data["RequestedBy"]
    if "CreatedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["created_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    else:
        import datetime

        out["created_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if "CreatedBy" in data:
        out["created_by"] = data["CreatedBy"]
    else:
        out["created_by"] = "n/a"
    if "ReviewRequestComments" in data:
        import aws_sdk_connect.types.evaluation_review_request_comment_list

        out["review_request_comments"] = (
            aws_sdk_connect.types.evaluation_review_request_comment_list.deserialize_json(
                data["ReviewRequestComments"]
            )
        )
    else:
        raise DeserializationError(
            "EvaluationReviewMetadata.review_request_comments required"
        )
    return out
