"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CollaborationConfiguredAudienceModelAssociationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.collaboration_configured_audience_model_association_summary

CollaborationConfiguredAudienceModelAssociationSummaryList: TypeAlias = list[
    "aws_sdk_cleanrooms.types.collaboration_configured_audience_model_association_summary.CollaborationConfiguredAudienceModelAssociationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: CollaborationConfiguredAudienceModelAssociationSummaryList,
) -> list:
    import aws_sdk_cleanrooms.types.collaboration_configured_audience_model_association_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cleanrooms.types.collaboration_configured_audience_model_association_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> CollaborationConfiguredAudienceModelAssociationSummaryList:
    import aws_sdk_cleanrooms.types.collaboration_configured_audience_model_association_summary

    out: CollaborationConfiguredAudienceModelAssociationSummaryList = []
    for item in data:
        out.append(
            aws_sdk_cleanrooms.types.collaboration_configured_audience_model_association_summary.deserialize_json(
                item
            )
        )
    return out
