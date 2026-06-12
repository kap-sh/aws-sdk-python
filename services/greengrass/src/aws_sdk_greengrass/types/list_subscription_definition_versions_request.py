"""Generated from Smithy shape ``com.amazonaws.greengrass#ListSubscriptionDefinitionVersionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string


class ListSubscriptionDefinitionVersionsRequest(TypedDict):
    max_results: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The maximum number of results to be returned per request."""
    next_token: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The token for the next set of results, or ''null'' if there are no additional results."""
    subscription_definition_id: "aws_sdk_greengrass.types.__string.__string"
    """The ID of the subscription definition."""


# --- restJson1 ser/de ---
def serialize_json(value: ListSubscriptionDefinitionVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSubscriptionDefinitionVersionsRequest:
    out: ListSubscriptionDefinitionVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
