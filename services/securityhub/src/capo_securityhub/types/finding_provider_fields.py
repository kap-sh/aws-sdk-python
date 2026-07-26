"""Generated from Smithy shape ``com.amazonaws.securityhub#FindingProviderFields``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.finding_provider_severity
    import capo_securityhub.types.ratio_scale
    import capo_securityhub.types.related_finding_list
    import capo_securityhub.types.type_list


class FindingProviderFields(TypedDict, closed=True):
    confidence: NotRequired["capo_securityhub.types.ratio_scale.RatioScale"]
    """<p>A finding's confidence. Confidence is defined as the likelihood that a finding accurately identifies the behavior or issue that it was intended to identify.</p> <p>Confidence is scored on a 0-100 basis using a ratio scale, where 0 means zero percent confidence and 100 means 100 percent confidence.</p>"""
    criticality: NotRequired["capo_securityhub.types.ratio_scale.RatioScale"]
    """<p>The level of importance assigned to the resources associated with the finding.</p> <p>A score of 0 means that the underlying resources have no criticality, and a score of 100 is reserved for the most critical resources.</p>"""
    related_findings: NotRequired[
        "capo_securityhub.types.related_finding_list.RelatedFindingList"
    ]
    """<p>A list of findings that are related to the current finding.</p>"""
    severity: NotRequired[
        "capo_securityhub.types.finding_provider_severity.FindingProviderSeverity"
    ]
    """<p>The severity of a finding.</p>"""
    types: NotRequired["capo_securityhub.types.type_list.TypeList"]
    """<p>One or more finding types in the format of <code>namespace/category/classifier</code> that classify a finding.</p> <p>Valid namespace values are: Software and Configuration Checks | TTPs | Effects | Unusual Behaviors | Sensitive Data Identifications</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FindingProviderFields) -> dict:
    out: dict = {}
    if "confidence" in value:
        out["Confidence"] = value["confidence"]
    if "criticality" in value:
        out["Criticality"] = value["criticality"]
    if "related_findings" in value:
        import capo_securityhub.types.related_finding_list

        out["RelatedFindings"] = (
            capo_securityhub.types.related_finding_list.serialize_json(
                value["related_findings"]
            )
        )
    if "severity" in value:
        import capo_securityhub.types.finding_provider_severity

        out["Severity"] = (
            capo_securityhub.types.finding_provider_severity.serialize_json(
                value["severity"]
            )
        )
    if "types" in value:
        import capo_securityhub.types.type_list

        out["Types"] = capo_securityhub.types.type_list.serialize_json(value["types"])
    return out


def deserialize_json(data: dict) -> FindingProviderFields:
    out: FindingProviderFields = {}  # type: ignore[typeddict-item]
    if "Confidence" in data:
        out["confidence"] = data["Confidence"]
    if "Criticality" in data:
        out["criticality"] = data["Criticality"]
    if "RelatedFindings" in data:
        import capo_securityhub.types.related_finding_list

        out["related_findings"] = (
            capo_securityhub.types.related_finding_list.deserialize_json(
                data["RelatedFindings"]
            )
        )
    if "Severity" in data:
        import capo_securityhub.types.finding_provider_severity

        out["severity"] = (
            capo_securityhub.types.finding_provider_severity.deserialize_json(
                data["Severity"]
            )
        )
    if "Types" in data:
        import capo_securityhub.types.type_list

        out["types"] = capo_securityhub.types.type_list.deserialize_json(data["Types"])
    return out
