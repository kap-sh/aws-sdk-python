"""Generated from Smithy shape ``com.amazonaws.securityhub#GetInsightResultsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class GetInsightResultsRequest(TypedDict, closed=True):
    insight_arn: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    """<p>The ARN of the insight for which to return results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetInsightResultsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetInsightResultsRequest:
    out: GetInsightResultsRequest = {}  # type: ignore[typeddict-item]
    return out
