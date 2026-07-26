"""Generated from Smithy shape ``com.amazonaws.pinpoint#CreateRecommenderConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.create_recommender_configuration_shape


class CreateRecommenderConfigurationRequest(TypedDict, closed=True):
    create_recommender_configuration: NotRequired[
        "capo_pinpoint.types.create_recommender_configuration_shape.CreateRecommenderConfigurationShape"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: CreateRecommenderConfigurationRequest) -> dict:
    out: dict = {}
    if "create_recommender_configuration" in value:
        import capo_pinpoint.types.create_recommender_configuration_shape

        out["CreateRecommenderConfiguration"] = (
            capo_pinpoint.types.create_recommender_configuration_shape.serialize_json(
                value["create_recommender_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateRecommenderConfigurationRequest:
    out: CreateRecommenderConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "CreateRecommenderConfiguration" in data:
        import capo_pinpoint.types.create_recommender_configuration_shape

        out["create_recommender_configuration"] = (
            capo_pinpoint.types.create_recommender_configuration_shape.deserialize_json(
                data["CreateRecommenderConfiguration"]
            )
        )
    return out
