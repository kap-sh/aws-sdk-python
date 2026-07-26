"""Generated from Smithy shape ``com.amazonaws.customerprofiles#RecommenderSchemaSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.recommender_schema_summary

RecommenderSchemaSummaryList: TypeAlias = list[
    "capo_customer_profiles.types.recommender_schema_summary.RecommenderSchemaSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommenderSchemaSummaryList) -> list:
    import capo_customer_profiles.types.recommender_schema_summary

    out: list = []
    for item in value:
        out.append(
            capo_customer_profiles.types.recommender_schema_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RecommenderSchemaSummaryList:
    import capo_customer_profiles.types.recommender_schema_summary

    out: RecommenderSchemaSummaryList = []
    for item in data:
        out.append(
            capo_customer_profiles.types.recommender_schema_summary.deserialize_json(
                item
            )
        )
    return out
