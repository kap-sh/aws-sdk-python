"""Generated from Smithy shape ``com.amazonaws.eks#InsightStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.insight_status_value
    import aws_sdk_eks.types.string


class InsightStatus(TypedDict, closed=True):
    status: NotRequired["aws_sdk_eks.types.insight_status_value.InsightStatusValue"]
    """<p>The status of the resource.</p>"""
    reason: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>Explanation on the reasoning for the status of the resource. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InsightStatus) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_eks.types.insight_status_value

        out["status"] = aws_sdk_eks.types.insight_status_value.serialize_json(
            value["status"]
        )
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> InsightStatus:
    out: InsightStatus = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_eks.types.insight_status_value

        out["status"] = aws_sdk_eks.types.insight_status_value.deserialize_json(
            data["status"]
        )
    if "reason" in data:
        out["reason"] = data["reason"]
    return out
