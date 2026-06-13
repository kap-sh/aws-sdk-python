"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ConfiguredAudienceModelAssociationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.configured_audience_model_association_summary

ConfiguredAudienceModelAssociationSummaryList: TypeAlias = list[
    "aws_sdk_cleanrooms.types.configured_audience_model_association_summary.ConfiguredAudienceModelAssociationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfiguredAudienceModelAssociationSummaryList) -> list:
    import aws_sdk_cleanrooms.types.configured_audience_model_association_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cleanrooms.types.configured_audience_model_association_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ConfiguredAudienceModelAssociationSummaryList:
    import aws_sdk_cleanrooms.types.configured_audience_model_association_summary

    out: ConfiguredAudienceModelAssociationSummaryList = []
    for item in data:
        out.append(
            aws_sdk_cleanrooms.types.configured_audience_model_association_summary.deserialize_json(
                item
            )
        )
    return out
