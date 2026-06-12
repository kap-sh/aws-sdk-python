"""Generated from Smithy shape ``com.amazonaws.pinpoint#DeleteRecommenderConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string


class DeleteRecommenderConfigurationRequest(TypedDict):
    recommender_id: "aws_sdk_pinpoint.types.__string.__string"
    """<p>The unique identifier for the recommender model configuration. This identifier is displayed as the <b>Recommender ID</b> on the Amazon Pinpoint console.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRecommenderConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRecommenderConfigurationRequest:
    out: DeleteRecommenderConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
