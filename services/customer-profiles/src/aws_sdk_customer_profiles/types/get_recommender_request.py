"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetRecommenderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.get_recommender_request_training_metrics_count_integer
    import aws_sdk_customer_profiles.types.name


class GetRecommenderRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    recommender_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The name of the recommender.</p>"""
    training_metrics_count: NotRequired[
        "aws_sdk_customer_profiles.types.get_recommender_request_training_metrics_count_integer.GetRecommenderRequestTrainingMetricsCountInteger"
    ]
    """<p>The number of training metrics to retrieve for the recommender.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRecommenderRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRecommenderRequest:
    out: GetRecommenderRequest = {}  # type: ignore[typeddict-item]
    return out
