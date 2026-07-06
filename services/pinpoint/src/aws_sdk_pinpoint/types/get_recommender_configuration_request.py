"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetRecommenderConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string


class GetRecommenderConfigurationRequest(TypedDict, closed=True):
    recommender_id: "aws_sdk_pinpoint.types.__string.__string"
    """<p>The unique identifier for the recommender model configuration. This identifier is displayed as the <b>Recommender ID</b> on the Amazon Pinpoint console.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRecommenderConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRecommenderConfigurationRequest:
    out: GetRecommenderConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
