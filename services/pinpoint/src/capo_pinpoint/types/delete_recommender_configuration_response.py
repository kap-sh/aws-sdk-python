"""Generated from Smithy shape ``com.amazonaws.pinpoint#DeleteRecommenderConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.recommender_configuration_response


class DeleteRecommenderConfigurationResponse(TypedDict, closed=True):
    recommender_configuration_response: NotRequired[
        "capo_pinpoint.types.recommender_configuration_response.RecommenderConfigurationResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRecommenderConfigurationResponse) -> dict:
    out: dict = {}
    if "recommender_configuration_response" in value:
        import capo_pinpoint.types.recommender_configuration_response

        out["RecommenderConfigurationResponse"] = (
            capo_pinpoint.types.recommender_configuration_response.serialize_json(
                value["recommender_configuration_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteRecommenderConfigurationResponse:
    out: DeleteRecommenderConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "RecommenderConfigurationResponse" in data:
        import capo_pinpoint.types.recommender_configuration_response

        out["recommender_configuration_response"] = (
            capo_pinpoint.types.recommender_configuration_response.deserialize_json(
                data["RecommenderConfigurationResponse"]
            )
        )
    return out
