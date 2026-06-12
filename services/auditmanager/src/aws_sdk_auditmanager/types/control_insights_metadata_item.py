"""Generated from Smithy shape ``com.amazonaws.auditmanager#ControlInsightsMetadataItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.control_domain_id
    import aws_sdk_auditmanager.types.evidence_insights
    import aws_sdk_auditmanager.types.string
    import aws_sdk_auditmanager.types.timestamp


class ControlInsightsMetadataItem(TypedDict):
    name: NotRequired["aws_sdk_auditmanager.types.string.String"]
    """<p>The name of the control. </p>"""
    id: NotRequired["aws_sdk_auditmanager.types.control_domain_id.ControlDomainId"]
    """<p>The unique identifier for the control. </p>"""
    evidence_insights: NotRequired[
        "aws_sdk_auditmanager.types.evidence_insights.EvidenceInsights"
    ]
    """<p>A breakdown of the compliance check status for the evidence that’s associated with the control. </p>"""
    last_updated: NotRequired["aws_sdk_auditmanager.types.timestamp.Timestamp"]
    """<p>The time when the control insights were last updated. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ControlInsightsMetadataItem) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "id" in value:
        out["id"] = value["id"]
    if "evidence_insights" in value:
        import aws_sdk_auditmanager.types.evidence_insights

        out["evidenceInsights"] = (
            aws_sdk_auditmanager.types.evidence_insights.serialize_json(
                value["evidence_insights"]
            )
        )
    if "last_updated" in value:
        import aws_sdk_auditmanager.types.timestamp

        out["lastUpdated"] = aws_sdk_auditmanager.types.timestamp.serialize_json(
            value["last_updated"]
        )
    return out


def deserialize_json(data: dict) -> ControlInsightsMetadataItem:
    out: ControlInsightsMetadataItem = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "id" in data:
        out["id"] = data["id"]
    if "evidenceInsights" in data:
        import aws_sdk_auditmanager.types.evidence_insights

        out["evidence_insights"] = (
            aws_sdk_auditmanager.types.evidence_insights.deserialize_json(
                data["evidenceInsights"]
            )
        )
    if "lastUpdated" in data:
        import aws_sdk_auditmanager.types.timestamp

        out["last_updated"] = aws_sdk_auditmanager.types.timestamp.deserialize_json(
            data["lastUpdated"]
        )
    return out
