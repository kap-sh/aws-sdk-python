"""Generated from Smithy shape ``com.amazonaws.customerprofiles#RecommenderPromotionalFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.recommender_promotional_filter

RecommenderPromotionalFilters: TypeAlias = list[
    "aws_sdk_customer_profiles.types.recommender_promotional_filter.RecommenderPromotionalFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommenderPromotionalFilters) -> list:
    import aws_sdk_customer_profiles.types.recommender_promotional_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_customer_profiles.types.recommender_promotional_filter.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RecommenderPromotionalFilters:
    import aws_sdk_customer_profiles.types.recommender_promotional_filter

    out: RecommenderPromotionalFilters = []
    for item in data:
        out.append(
            aws_sdk_customer_profiles.types.recommender_promotional_filter.deserialize_json(
                item
            )
        )
    return out
