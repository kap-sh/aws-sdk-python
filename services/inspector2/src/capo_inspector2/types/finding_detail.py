"""Generated from Smithy shape ``com.amazonaws.inspector2#FindingDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.cisa_data
    import capo_inspector2.types.cwes
    import capo_inspector2.types.evidence_list
    import capo_inspector2.types.exploit_observed
    import capo_inspector2.types.finding_arn
    import capo_inspector2.types.risk_score
    import capo_inspector2.types.tools
    import capo_inspector2.types.ttps
    import capo_inspector2.types.vulnerability_reference_urls


class FindingDetail(TypedDict, closed=True):
    finding_arn: NotRequired["capo_inspector2.types.finding_arn.FindingArn"]
    """<p>The finding ARN that the vulnerability details are associated with.</p>"""
    cisa_data: NotRequired["capo_inspector2.types.cisa_data.CisaData"]
    """<p>The Cybersecurity and Infrastructure Security Agency (CISA) details for a specific vulnerability.</p>"""
    risk_score: NotRequired["capo_inspector2.types.risk_score.RiskScore"]
    """<p>The risk score of the vulnerability.</p>"""
    evidences: NotRequired["capo_inspector2.types.evidence_list.EvidenceList"]
    """<p>Information on the evidence of the vulnerability.</p>"""
    ttps: NotRequired["capo_inspector2.types.ttps.Ttps"]
    """<p>The MITRE adversary tactics, techniques, or procedures (TTPs) associated with the vulnerability.</p>"""
    tools: NotRequired["capo_inspector2.types.tools.Tools"]
    """<p>The known malware tools or kits that can exploit the vulnerability.</p>"""
    exploit_observed: NotRequired[
        "capo_inspector2.types.exploit_observed.ExploitObserved"
    ]
    """<p>Contains information on when this exploit was observed.</p>"""
    reference_urls: NotRequired[
        "capo_inspector2.types.vulnerability_reference_urls.VulnerabilityReferenceUrls"
    ]
    """<p>The reference URLs for the vulnerability data.</p>"""
    cwes: NotRequired["capo_inspector2.types.cwes.Cwes"]
    """<p>The Common Weakness Enumerations (CWEs) associated with the vulnerability.</p>"""
    epss_score: NotRequired["float"]
    """<p>The Exploit Prediction Scoring System (EPSS) score of the vulnerability.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FindingDetail) -> dict:
    out: dict = {}
    if "finding_arn" in value:
        out["findingArn"] = value["finding_arn"]
    if "cisa_data" in value:
        import capo_inspector2.types.cisa_data

        out["cisaData"] = capo_inspector2.types.cisa_data.serialize_json(
            value["cisa_data"]
        )
    if "risk_score" in value:
        out["riskScore"] = value["risk_score"]
    if "evidences" in value:
        import capo_inspector2.types.evidence_list

        out["evidences"] = capo_inspector2.types.evidence_list.serialize_json(
            value["evidences"]
        )
    if "ttps" in value:
        import capo_inspector2.types.ttps

        out["ttps"] = capo_inspector2.types.ttps.serialize_json(value["ttps"])
    if "tools" in value:
        import capo_inspector2.types.tools

        out["tools"] = capo_inspector2.types.tools.serialize_json(value["tools"])
    if "exploit_observed" in value:
        import capo_inspector2.types.exploit_observed

        out["exploitObserved"] = capo_inspector2.types.exploit_observed.serialize_json(
            value["exploit_observed"]
        )
    if "reference_urls" in value:
        import capo_inspector2.types.vulnerability_reference_urls

        out["referenceUrls"] = (
            capo_inspector2.types.vulnerability_reference_urls.serialize_json(
                value["reference_urls"]
            )
        )
    if "cwes" in value:
        import capo_inspector2.types.cwes

        out["cwes"] = capo_inspector2.types.cwes.serialize_json(value["cwes"])
    if "epss_score" in value:
        out["epssScore"] = value["epss_score"]
    return out


def deserialize_json(data: dict) -> FindingDetail:
    out: FindingDetail = {}  # type: ignore[typeddict-item]
    if "findingArn" in data:
        out["finding_arn"] = data["findingArn"]
    if "cisaData" in data:
        import capo_inspector2.types.cisa_data

        out["cisa_data"] = capo_inspector2.types.cisa_data.deserialize_json(
            data["cisaData"]
        )
    if "riskScore" in data:
        out["risk_score"] = data["riskScore"]
    if "evidences" in data:
        import capo_inspector2.types.evidence_list

        out["evidences"] = capo_inspector2.types.evidence_list.deserialize_json(
            data["evidences"]
        )
    if "ttps" in data:
        import capo_inspector2.types.ttps

        out["ttps"] = capo_inspector2.types.ttps.deserialize_json(data["ttps"])
    if "tools" in data:
        import capo_inspector2.types.tools

        out["tools"] = capo_inspector2.types.tools.deserialize_json(data["tools"])
    if "exploitObserved" in data:
        import capo_inspector2.types.exploit_observed

        out["exploit_observed"] = (
            capo_inspector2.types.exploit_observed.deserialize_json(
                data["exploitObserved"]
            )
        )
    if "referenceUrls" in data:
        import capo_inspector2.types.vulnerability_reference_urls

        out["reference_urls"] = (
            capo_inspector2.types.vulnerability_reference_urls.deserialize_json(
                data["referenceUrls"]
            )
        )
    if "cwes" in data:
        import capo_inspector2.types.cwes

        out["cwes"] = capo_inspector2.types.cwes.deserialize_json(data["cwes"])
    if "epssScore" in data:
        out["epss_score"] = data["epssScore"]
    return out
