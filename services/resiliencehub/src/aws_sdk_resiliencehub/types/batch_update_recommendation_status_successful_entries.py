"""Generated from Smithy shape ``com.amazonaws.resiliencehub#BatchUpdateRecommendationStatusSuccessfulEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.batch_update_recommendation_status_successful_entry

BatchUpdateRecommendationStatusSuccessfulEntries: TypeAlias = list[
    "aws_sdk_resiliencehub.types.batch_update_recommendation_status_successful_entry.BatchUpdateRecommendationStatusSuccessfulEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateRecommendationStatusSuccessfulEntries) -> list:
    import aws_sdk_resiliencehub.types.batch_update_recommendation_status_successful_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_resiliencehub.types.batch_update_recommendation_status_successful_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchUpdateRecommendationStatusSuccessfulEntries:
    import aws_sdk_resiliencehub.types.batch_update_recommendation_status_successful_entry

    out: BatchUpdateRecommendationStatusSuccessfulEntries = []
    for item in data:
        out.append(
            aws_sdk_resiliencehub.types.batch_update_recommendation_status_successful_entry.deserialize_json(
                item
            )
        )
    return out
