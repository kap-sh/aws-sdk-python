"""Generated from Smithy shape ``com.amazonaws.pinpoint#UpdateRecommenderConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.update_recommender_configuration_shape


class UpdateRecommenderConfigurationRequest(TypedDict, closed=True):
    recommender_id: "capo_pinpoint.types.__string.__string"
    """<p>The unique identifier for the recommender model configuration. This identifier is displayed as the <b>Recommender ID</b> on the Amazon Pinpoint console.</p>"""
    update_recommender_configuration: NotRequired[
        "capo_pinpoint.types.update_recommender_configuration_shape.UpdateRecommenderConfigurationShape"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRecommenderConfigurationRequest) -> dict:
    out: dict = {}
    if "update_recommender_configuration" in value:
        import capo_pinpoint.types.update_recommender_configuration_shape

        out["UpdateRecommenderConfiguration"] = (
            capo_pinpoint.types.update_recommender_configuration_shape.serialize_json(
                value["update_recommender_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateRecommenderConfigurationRequest:
    out: UpdateRecommenderConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "UpdateRecommenderConfiguration" in data:
        import capo_pinpoint.types.update_recommender_configuration_shape

        out["update_recommender_configuration"] = (
            capo_pinpoint.types.update_recommender_configuration_shape.deserialize_json(
                data["UpdateRecommenderConfiguration"]
            )
        )
    return out
