"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourceFindingsSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.integer
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.resource_severity_breakdown


class ResourceFindingsSummary(TypedDict, closed=True):
    finding_type: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The category or classification of the security finding.</p>"""
    product_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the product associated with the security finding.</p>"""
    total_findings: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The total count of security findings.</p>"""
    severities: NotRequired[
        "capo_securityhub.types.resource_severity_breakdown.ResourceSeverityBreakdown"
    ]
    """<p>A breakdown of security findings by their severity levels.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceFindingsSummary) -> dict:
    out: dict = {}
    if "finding_type" in value:
        out["FindingType"] = value["finding_type"]
    if "product_name" in value:
        out["ProductName"] = value["product_name"]
    if "total_findings" in value:
        out["TotalFindings"] = value["total_findings"]
    if "severities" in value:
        import capo_securityhub.types.resource_severity_breakdown

        out["Severities"] = (
            capo_securityhub.types.resource_severity_breakdown.serialize_json(
                value["severities"]
            )
        )
    return out


def deserialize_json(data: dict) -> ResourceFindingsSummary:
    out: ResourceFindingsSummary = {}  # type: ignore[typeddict-item]
    if "FindingType" in data:
        out["finding_type"] = data["FindingType"]
    if "ProductName" in data:
        out["product_name"] = data["ProductName"]
    if "TotalFindings" in data:
        out["total_findings"] = data["TotalFindings"]
    if "Severities" in data:
        import capo_securityhub.types.resource_severity_breakdown

        out["severities"] = (
            capo_securityhub.types.resource_severity_breakdown.deserialize_json(
                data["Severities"]
            )
        )
    return out
