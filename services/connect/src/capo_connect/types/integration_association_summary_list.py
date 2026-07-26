"""Generated from Smithy shape ``com.amazonaws.connect#IntegrationAssociationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.integration_association_summary

IntegrationAssociationSummaryList: TypeAlias = list[
    "capo_connect.types.integration_association_summary.IntegrationAssociationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: IntegrationAssociationSummaryList) -> list:
    import capo_connect.types.integration_association_summary

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.integration_association_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> IntegrationAssociationSummaryList:
    import capo_connect.types.integration_association_summary

    out: IntegrationAssociationSummaryList = []
    for item in data:
        out.append(
            capo_connect.types.integration_association_summary.deserialize_json(item)
        )
    return out
