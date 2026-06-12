"""Generated from Smithy shape ``com.amazonaws.sesv2#ListRecommendationsFilter``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.list_recommendation_filter_value
    import aws_sdk_sesv2.types.list_recommendations_filter_key

ListRecommendationsFilter: TypeAlias = dict[
    "aws_sdk_sesv2.types.list_recommendations_filter_key.ListRecommendationsFilterKey",
    "aws_sdk_sesv2.types.list_recommendation_filter_value.ListRecommendationFilterValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ListRecommendationsFilter) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_sesv2.types.list_recommendations_filter_key

        out[aws_sdk_sesv2.types.list_recommendations_filter_key.serialize_json(key)] = (
            value
        )
    return out


def deserialize_json(data: dict) -> ListRecommendationsFilter:
    out: ListRecommendationsFilter = {}
    for key, value in data.items():
        import aws_sdk_sesv2.types.list_recommendations_filter_key

        out[
            aws_sdk_sesv2.types.list_recommendations_filter_key.deserialize_json(key)
        ] = value
    return out
