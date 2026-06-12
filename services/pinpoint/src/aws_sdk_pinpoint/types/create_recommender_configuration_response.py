"""Generated from Smithy shape ``com.amazonaws.pinpoint#CreateRecommenderConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.recommender_configuration_response


class CreateRecommenderConfigurationResponse(TypedDict):
    recommender_configuration_response: NotRequired[
        "aws_sdk_pinpoint.types.recommender_configuration_response.RecommenderConfigurationResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: CreateRecommenderConfigurationResponse) -> dict:
    out: dict = {}
    if "recommender_configuration_response" in value:
        import aws_sdk_pinpoint.types.recommender_configuration_response

        out["RecommenderConfigurationResponse"] = (
            aws_sdk_pinpoint.types.recommender_configuration_response.serialize_json(
                value["recommender_configuration_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateRecommenderConfigurationResponse:
    out: CreateRecommenderConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "RecommenderConfigurationResponse" in data:
        import aws_sdk_pinpoint.types.recommender_configuration_response

        out["recommender_configuration_response"] = (
            aws_sdk_pinpoint.types.recommender_configuration_response.deserialize_json(
                data["RecommenderConfigurationResponse"]
            )
        )
    return out
