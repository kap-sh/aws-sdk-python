"""Generated from Smithy shape ``com.amazonaws.customerprofiles#RecommenderFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.recommender_filter

RecommenderFilters: TypeAlias = list[
    "aws_sdk_customer_profiles.types.recommender_filter.RecommenderFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommenderFilters) -> list:
    import aws_sdk_customer_profiles.types.recommender_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_customer_profiles.types.recommender_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RecommenderFilters:
    import aws_sdk_customer_profiles.types.recommender_filter

    out: RecommenderFilters = []
    for item in data:
        out.append(
            aws_sdk_customer_profiles.types.recommender_filter.deserialize_json(item)
        )
    return out
