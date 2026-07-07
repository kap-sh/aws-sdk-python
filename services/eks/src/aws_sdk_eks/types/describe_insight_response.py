"""Generated from Smithy shape ``com.amazonaws.eks#DescribeInsightResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.insight


class DescribeInsightResponse(TypedDict, closed=True):
    insight: NotRequired["aws_sdk_eks.types.insight.Insight"]
    """<p>The full description of the insight.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeInsightResponse) -> dict:
    out: dict = {}
    if "insight" in value:
        import aws_sdk_eks.types.insight

        out["insight"] = aws_sdk_eks.types.insight.serialize_json(value["insight"])
    return out


def deserialize_json(data: dict) -> DescribeInsightResponse:
    out: DescribeInsightResponse = {}  # type: ignore[typeddict-item]
    if "insight" in data:
        import aws_sdk_eks.types.insight

        out["insight"] = aws_sdk_eks.types.insight.deserialize_json(data["insight"])
    return out
