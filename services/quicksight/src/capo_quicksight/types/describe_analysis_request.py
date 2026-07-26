"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeAnalysisRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.short_restrictive_resource_id


class DescribeAnalysisRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the analysis. You must be using the Amazon Web Services account that the analysis is in.</p>"""
    analysis_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID of the analysis that you're describing. The ID is part of the URL of the analysis.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAnalysisRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeAnalysisRequest:
    out: DescribeAnalysisRequest = {}  # type: ignore[typeddict-item]
    return out
