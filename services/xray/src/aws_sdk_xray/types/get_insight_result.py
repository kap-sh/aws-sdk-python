"""Generated from Smithy shape ``com.amazonaws.xray#GetInsightResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_xray.types.insight


class GetInsightResult(TypedDict, closed=True):
    insight: NotRequired["aws_sdk_xray.types.insight.Insight"]
    """<p>The summary information of an insight.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetInsightResult) -> dict:
    out: dict = {}
    if "insight" in value:
        import aws_sdk_xray.types.insight

        out["Insight"] = aws_sdk_xray.types.insight.serialize_json(value["insight"])
    return out


def deserialize_json(data: dict) -> GetInsightResult:
    out: GetInsightResult = {}  # type: ignore[typeddict-item]
    if "Insight" in data:
        import aws_sdk_xray.types.insight

        out["insight"] = aws_sdk_xray.types.insight.deserialize_json(data["Insight"])
    return out
