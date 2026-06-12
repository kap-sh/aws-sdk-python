"""Generated from Smithy shape ``com.amazonaws.resiliencehub#BatchUpdateRecommendationStatusFailedEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.batch_update_recommendation_status_failed_entry

BatchUpdateRecommendationStatusFailedEntries: TypeAlias = list[
    "aws_sdk_resiliencehub.types.batch_update_recommendation_status_failed_entry.BatchUpdateRecommendationStatusFailedEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateRecommendationStatusFailedEntries) -> list:
    import aws_sdk_resiliencehub.types.batch_update_recommendation_status_failed_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_resiliencehub.types.batch_update_recommendation_status_failed_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchUpdateRecommendationStatusFailedEntries:
    import aws_sdk_resiliencehub.types.batch_update_recommendation_status_failed_entry

    out: BatchUpdateRecommendationStatusFailedEntries = []
    for item in data:
        out.append(
            aws_sdk_resiliencehub.types.batch_update_recommendation_status_failed_entry.deserialize_json(
                item
            )
        )
    return out
