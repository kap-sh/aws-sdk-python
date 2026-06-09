"""Generated from Smithy shape ``com.amazonaws.eks#DescribeInsightsRefreshResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.insights_refresh_status
    import aws_sdk_eks.types.string
    import aws_sdk_eks.types.timestamp


class DescribeInsightsRefreshResponse(TypedDict):
    message: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The message associated with the insights refresh operation.</p>"""
    status: NotRequired[
        "aws_sdk_eks.types.insights_refresh_status.InsightsRefreshStatus"
    ]
    """<p>The current status of the insights refresh operation.</p>"""
    started_at: NotRequired["aws_sdk_eks.types.timestamp.Timestamp"]
    """<p>The date and time when the insights refresh operation started.</p>"""
    ended_at: NotRequired["aws_sdk_eks.types.timestamp.Timestamp"]
    """<p>The date and time when the insights refresh operation ended.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeInsightsRefreshResponse) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "status" in value:
        import aws_sdk_eks.types.insights_refresh_status

        out["status"] = aws_sdk_eks.types.insights_refresh_status.serialize_json(
            value["status"]
        )
    if "started_at" in value:
        import aws_sdk_eks.types.timestamp

        out["startedAt"] = aws_sdk_eks.types.timestamp.serialize_json(
            value["started_at"]
        )
    if "ended_at" in value:
        import aws_sdk_eks.types.timestamp

        out["endedAt"] = aws_sdk_eks.types.timestamp.serialize_json(value["ended_at"])
    return out


def deserialize_json(data: dict) -> DescribeInsightsRefreshResponse:
    out: DescribeInsightsRefreshResponse = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "status" in data:
        import aws_sdk_eks.types.insights_refresh_status

        out["status"] = aws_sdk_eks.types.insights_refresh_status.deserialize_json(
            data["status"]
        )
    if "startedAt" in data:
        import aws_sdk_eks.types.timestamp

        out["started_at"] = aws_sdk_eks.types.timestamp.deserialize_json(
            data["startedAt"]
        )
    if "endedAt" in data:
        import aws_sdk_eks.types.timestamp

        out["ended_at"] = aws_sdk_eks.types.timestamp.deserialize_json(data["endedAt"])
    return out
