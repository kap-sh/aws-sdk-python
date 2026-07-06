"""Generated from Smithy shape ``com.amazonaws.securityhub#CreateInsightResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class CreateInsightResponse(TypedDict, closed=True):
    insight_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the insight created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateInsightResponse) -> dict:
    out: dict = {}
    if "insight_arn" in value:
        out["InsightArn"] = value["insight_arn"]
    return out


def deserialize_json(data: dict) -> CreateInsightResponse:
    out: CreateInsightResponse = {}  # type: ignore[typeddict-item]
    if "InsightArn" in data:
        out["insight_arn"] = data["InsightArn"]
    return out
