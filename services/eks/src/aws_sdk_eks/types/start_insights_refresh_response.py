"""Generated from Smithy shape ``com.amazonaws.eks#StartInsightsRefreshResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.insights_refresh_status
    import aws_sdk_eks.types.string


class StartInsightsRefreshResponse(TypedDict):
    message: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The message associated with the insights refresh operation.</p>"""
    status: NotRequired[
        "aws_sdk_eks.types.insights_refresh_status.InsightsRefreshStatus"
    ]
    """<p>The current status of the insights refresh operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartInsightsRefreshResponse) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "status" in value:
        import aws_sdk_eks.types.insights_refresh_status

        out["status"] = aws_sdk_eks.types.insights_refresh_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> StartInsightsRefreshResponse:
    out: StartInsightsRefreshResponse = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "status" in data:
        import aws_sdk_eks.types.insights_refresh_status

        out["status"] = aws_sdk_eks.types.insights_refresh_status.deserialize_json(
            data["status"]
        )
    return out
