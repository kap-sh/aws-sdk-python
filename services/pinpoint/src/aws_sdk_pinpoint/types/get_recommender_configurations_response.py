"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetRecommenderConfigurationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.list_recommender_configurations_response


class GetRecommenderConfigurationsResponse(TypedDict, closed=True):
    list_recommender_configurations_response: NotRequired[
        "aws_sdk_pinpoint.types.list_recommender_configurations_response.ListRecommenderConfigurationsResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetRecommenderConfigurationsResponse) -> dict:
    out: dict = {}
    if "list_recommender_configurations_response" in value:
        import aws_sdk_pinpoint.types.list_recommender_configurations_response

        out["ListRecommenderConfigurationsResponse"] = (
            aws_sdk_pinpoint.types.list_recommender_configurations_response.serialize_json(
                value["list_recommender_configurations_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetRecommenderConfigurationsResponse:
    out: GetRecommenderConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if "ListRecommenderConfigurationsResponse" in data:
        import aws_sdk_pinpoint.types.list_recommender_configurations_response

        out["list_recommender_configurations_response"] = (
            aws_sdk_pinpoint.types.list_recommender_configurations_response.deserialize_json(
                data["ListRecommenderConfigurationsResponse"]
            )
        )
    return out
