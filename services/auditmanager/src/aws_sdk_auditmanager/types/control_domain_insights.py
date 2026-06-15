"""Generated from Smithy shape ``com.amazonaws.auditmanager#ControlDomainInsights``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.control_domain_id
    import aws_sdk_auditmanager.types.evidence_insights
    import aws_sdk_auditmanager.types.nullable_integer
    import aws_sdk_auditmanager.types.string
    import aws_sdk_auditmanager.types.timestamp


class ControlDomainInsights(TypedDict):
    name: NotRequired["aws_sdk_auditmanager.types.string.String"]
    """<p>The name of the control domain. </p>"""
    id: NotRequired["aws_sdk_auditmanager.types.control_domain_id.ControlDomainId"]
    r"""<p>The unique identifier for the control domain. Audit Manager supports the control domains that are provided by Amazon Web Services Control Catalog. For information about how to find a list of available control domains, see <a href=\"https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ListDomains.html\"> <code>ListDomains</code> </a> in the Amazon Web Services Control Catalog API Reference.</p>"""
    controls_count_by_noncompliant_evidence: NotRequired[
        "aws_sdk_auditmanager.types.nullable_integer.NullableInteger"
    ]
    """<p>The number of controls in the control domain that collected non-compliant evidence on the <code>lastUpdated</code> date. </p>"""
    total_controls_count: NotRequired[
        "aws_sdk_auditmanager.types.nullable_integer.NullableInteger"
    ]
    """<p>The total number of controls in the control domain. </p>"""
    evidence_insights: NotRequired[
        "aws_sdk_auditmanager.types.evidence_insights.EvidenceInsights"
    ]
    """<p>A breakdown of the compliance check status for the evidence that’s associated with the control domain. </p>"""
    last_updated: NotRequired["aws_sdk_auditmanager.types.timestamp.Timestamp"]
    """<p>The time when the control domain insights were last updated. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ControlDomainInsights) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "id" in value:
        out["id"] = value["id"]
    if "controls_count_by_noncompliant_evidence" in value:
        out["controlsCountByNoncompliantEvidence"] = value[
            "controls_count_by_noncompliant_evidence"
        ]
    if "total_controls_count" in value:
        out["totalControlsCount"] = value["total_controls_count"]
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


def deserialize_json(data: dict) -> ControlDomainInsights:
    out: ControlDomainInsights = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "id" in data:
        out["id"] = data["id"]
    if "controlsCountByNoncompliantEvidence" in data:
        out["controls_count_by_noncompliant_evidence"] = data[
            "controlsCountByNoncompliantEvidence"
        ]
    if "totalControlsCount" in data:
        out["total_controls_count"] = data["totalControlsCount"]
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
