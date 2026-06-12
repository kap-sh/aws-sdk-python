"""Generated from Smithy shape ``com.amazonaws.pinpoint#ListRecommenderConfigurationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.list_of_recommender_configuration_response


class ListRecommenderConfigurationsResponse(TypedDict):
    item: NotRequired[
        "aws_sdk_pinpoint.types.list_of_recommender_configuration_response.ListOfRecommenderConfigurationResponse"
    ]
    """<p>An array of responses, one for each recommender model configuration that's associated with your Amazon Pinpoint account.</p>"""
    next_token: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecommenderConfigurationsResponse) -> dict:
    out: dict = {}
    if "item" in value:
        import aws_sdk_pinpoint.types.list_of_recommender_configuration_response

        out["Item"] = (
            aws_sdk_pinpoint.types.list_of_recommender_configuration_response.serialize_json(
                value["item"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRecommenderConfigurationsResponse:
    out: ListRecommenderConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if "Item" in data:
        import aws_sdk_pinpoint.types.list_of_recommender_configuration_response

        out["item"] = (
            aws_sdk_pinpoint.types.list_of_recommender_configuration_response.deserialize_json(
                data["Item"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
