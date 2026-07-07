"""Generated from Smithy shape ``com.amazonaws.pinpoint#UpdateRecommenderConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.recommender_configuration_response


class UpdateRecommenderConfigurationResponse(TypedDict, closed=True):
    recommender_configuration_response: NotRequired[
        "aws_sdk_pinpoint.types.recommender_configuration_response.RecommenderConfigurationResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRecommenderConfigurationResponse) -> dict:
    out: dict = {}
    if "recommender_configuration_response" in value:
        import aws_sdk_pinpoint.types.recommender_configuration_response

        out["RecommenderConfigurationResponse"] = (
            aws_sdk_pinpoint.types.recommender_configuration_response.serialize_json(
                value["recommender_configuration_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateRecommenderConfigurationResponse:
    out: UpdateRecommenderConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "RecommenderConfigurationResponse" in data:
        import aws_sdk_pinpoint.types.recommender_configuration_response

        out["recommender_configuration_response"] = (
            aws_sdk_pinpoint.types.recommender_configuration_response.deserialize_json(
                data["RecommenderConfigurationResponse"]
            )
        )
    return out
