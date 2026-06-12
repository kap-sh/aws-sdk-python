"""Generated from Smithy shape ``com.amazonaws.pinpoint#ListOfRecommenderConfigurationResponse``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.recommender_configuration_response

ListOfRecommenderConfigurationResponse: TypeAlias = list[
    "aws_sdk_pinpoint.types.recommender_configuration_response.RecommenderConfigurationResponse"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfRecommenderConfigurationResponse) -> list:
    import aws_sdk_pinpoint.types.recommender_configuration_response

    out: list = []
    for item in value:
        out.append(
            aws_sdk_pinpoint.types.recommender_configuration_response.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ListOfRecommenderConfigurationResponse:
    import aws_sdk_pinpoint.types.recommender_configuration_response

    out: ListOfRecommenderConfigurationResponse = []
    for item in data:
        out.append(
            aws_sdk_pinpoint.types.recommender_configuration_response.deserialize_json(
                item
            )
        )
    return out
