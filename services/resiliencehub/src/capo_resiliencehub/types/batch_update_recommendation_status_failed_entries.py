"""Generated from Smithy shape ``com.amazonaws.resiliencehub#BatchUpdateRecommendationStatusFailedEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehub.types.batch_update_recommendation_status_failed_entry

BatchUpdateRecommendationStatusFailedEntries: TypeAlias = list[
    "capo_resiliencehub.types.batch_update_recommendation_status_failed_entry.BatchUpdateRecommendationStatusFailedEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateRecommendationStatusFailedEntries) -> list:
    import capo_resiliencehub.types.batch_update_recommendation_status_failed_entry

    out: list = []
    for item in value:
        out.append(
            capo_resiliencehub.types.batch_update_recommendation_status_failed_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchUpdateRecommendationStatusFailedEntries:
    import capo_resiliencehub.types.batch_update_recommendation_status_failed_entry

    out: BatchUpdateRecommendationStatusFailedEntries = []
    for item in data:
        out.append(
            capo_resiliencehub.types.batch_update_recommendation_status_failed_entry.deserialize_json(
                item
            )
        )
    return out
