"""Generated from Smithy shape ``com.amazonaws.pinpoint#ListOfRecommenderConfigurationResponse``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint.types.recommender_configuration_response

ListOfRecommenderConfigurationResponse: TypeAlias = list[
    "capo_pinpoint.types.recommender_configuration_response.RecommenderConfigurationResponse"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfRecommenderConfigurationResponse) -> list:
    import capo_pinpoint.types.recommender_configuration_response

    out: list = []
    for item in value:
        out.append(
            capo_pinpoint.types.recommender_configuration_response.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ListOfRecommenderConfigurationResponse:
    import capo_pinpoint.types.recommender_configuration_response

    out: ListOfRecommenderConfigurationResponse = []
    for item in data:
        out.append(
            capo_pinpoint.types.recommender_configuration_response.deserialize_json(
                item
            )
        )
    return out
