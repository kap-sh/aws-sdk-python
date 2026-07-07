"""Generated from Smithy shape ``com.amazonaws.lambda#ListCapacityProvidersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lambda.types.capacity_provider_state
    import aws_sdk_lambda.types.max_fifty_list_items
    import aws_sdk_lambda.types.string


class ListCapacityProvidersRequest(TypedDict, closed=True):
    state: NotRequired[
        "aws_sdk_lambda.types.capacity_provider_state.CapacityProviderState"
    ]
    """<p>Filter capacity providers by their current state.</p>"""
    marker: NotRequired["aws_sdk_lambda.types.string.String"]
    """<p>Specify the pagination token that's returned by a previous request to retrieve the next page of results.</p>"""
    max_items: NotRequired[
        "aws_sdk_lambda.types.max_fifty_list_items.MaxFiftyListItems"
    ]
    """<p>The maximum number of capacity providers to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCapacityProvidersRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCapacityProvidersRequest:
    out: ListCapacityProvidersRequest = {}  # type: ignore[typeddict-item]
    return out
