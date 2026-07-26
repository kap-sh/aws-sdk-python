"""Generated from Smithy shape ``com.amazonaws.appsync#SourceApiAssociationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appsync.types.source_api_association_summary

SourceApiAssociationSummaryList: TypeAlias = list[
    "capo_appsync.types.source_api_association_summary.SourceApiAssociationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: SourceApiAssociationSummaryList) -> list:
    import capo_appsync.types.source_api_association_summary

    out: list = []
    for item in value:
        out.append(
            capo_appsync.types.source_api_association_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SourceApiAssociationSummaryList:
    import capo_appsync.types.source_api_association_summary

    out: SourceApiAssociationSummaryList = []
    for item in data:
        out.append(
            capo_appsync.types.source_api_association_summary.deserialize_json(item)
        )
    return out
