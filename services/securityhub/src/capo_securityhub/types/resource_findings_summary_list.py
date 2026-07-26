"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourceFindingsSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.resource_findings_summary

ResourceFindingsSummaryList: TypeAlias = list[
    "capo_securityhub.types.resource_findings_summary.ResourceFindingsSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceFindingsSummaryList) -> list:
    import capo_securityhub.types.resource_findings_summary

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.resource_findings_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ResourceFindingsSummaryList:
    import capo_securityhub.types.resource_findings_summary

    out: ResourceFindingsSummaryList = []
    for item in data:
        out.append(
            capo_securityhub.types.resource_findings_summary.deserialize_json(item)
        )
    return out
