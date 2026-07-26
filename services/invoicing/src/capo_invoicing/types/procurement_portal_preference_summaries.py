"""Generated from Smithy shape ``com.amazonaws.invoicing#ProcurementPortalPreferenceSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_invoicing.types.procurement_portal_preference_summary

ProcurementPortalPreferenceSummaries: TypeAlias = list[
    "capo_invoicing.types.procurement_portal_preference_summary.ProcurementPortalPreferenceSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProcurementPortalPreferenceSummaries) -> list:
    import capo_invoicing.types.procurement_portal_preference_summary

    out: list = []
    for item in value:
        out.append(
            capo_invoicing.types.procurement_portal_preference_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ProcurementPortalPreferenceSummaries:
    import capo_invoicing.types.procurement_portal_preference_summary

    out: ProcurementPortalPreferenceSummaries = []
    for item in data:
        out.append(
            capo_invoicing.types.procurement_portal_preference_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
