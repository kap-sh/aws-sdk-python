"""Generated from Smithy shape ``com.amazonaws.securityhub#DeleteInsightResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class DeleteInsightResponse(TypedDict, closed=True):
    insight_arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the insight that was deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteInsightResponse) -> dict:
    out: dict = {}
    if "insight_arn" in value:
        out["InsightArn"] = value["insight_arn"]
    return out


def deserialize_json(data: dict) -> DeleteInsightResponse:
    out: DeleteInsightResponse = {}  # type: ignore[typeddict-item]
    if "InsightArn" in data:
        out["insight_arn"] = data["InsightArn"]
    return out
