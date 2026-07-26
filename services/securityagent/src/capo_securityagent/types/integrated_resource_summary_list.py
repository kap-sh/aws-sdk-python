"""Generated from Smithy shape ``com.amazonaws.securityagent#IntegratedResourceSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.integrated_resource_summary

IntegratedResourceSummaryList: TypeAlias = list[
    "capo_securityagent.types.integrated_resource_summary.IntegratedResourceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: IntegratedResourceSummaryList) -> list:
    import capo_securityagent.types.integrated_resource_summary

    out: list = []
    for item in value:
        out.append(
            capo_securityagent.types.integrated_resource_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> IntegratedResourceSummaryList:
    import capo_securityagent.types.integrated_resource_summary

    out: IntegratedResourceSummaryList = []
    for item in data:
        out.append(
            capo_securityagent.types.integrated_resource_summary.deserialize_json(item)
        )
    return out
