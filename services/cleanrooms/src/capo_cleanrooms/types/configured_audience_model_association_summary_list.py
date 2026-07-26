"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ConfiguredAudienceModelAssociationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.configured_audience_model_association_summary

ConfiguredAudienceModelAssociationSummaryList: TypeAlias = list[
    "capo_cleanrooms.types.configured_audience_model_association_summary.ConfiguredAudienceModelAssociationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfiguredAudienceModelAssociationSummaryList) -> list:
    import capo_cleanrooms.types.configured_audience_model_association_summary

    out: list = []
    for item in value:
        out.append(
            capo_cleanrooms.types.configured_audience_model_association_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ConfiguredAudienceModelAssociationSummaryList:
    import capo_cleanrooms.types.configured_audience_model_association_summary

    out: ConfiguredAudienceModelAssociationSummaryList = []
    for item in data:
        out.append(
            capo_cleanrooms.types.configured_audience_model_association_summary.deserialize_json(
                item
            )
        )
    return out
