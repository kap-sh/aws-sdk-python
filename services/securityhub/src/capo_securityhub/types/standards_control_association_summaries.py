"""Generated from Smithy shape ``com.amazonaws.securityhub#StandardsControlAssociationSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.standards_control_association_summary

StandardsControlAssociationSummaries: TypeAlias = list[
    "capo_securityhub.types.standards_control_association_summary.StandardsControlAssociationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: StandardsControlAssociationSummaries) -> list:
    import capo_securityhub.types.standards_control_association_summary

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.standards_control_association_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> StandardsControlAssociationSummaries:
    import capo_securityhub.types.standards_control_association_summary

    out: StandardsControlAssociationSummaries = []
    for item in data:
        out.append(
            capo_securityhub.types.standards_control_association_summary.deserialize_json(
                item
            )
        )
    return out
