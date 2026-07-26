"""Generated from Smithy shape ``com.amazonaws.lambda#ListFunctionVersionsByCapacityProviderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.capacity_provider_name
    import capo_lambda.types.max_fifty_list_items
    import capo_lambda.types.string


class ListFunctionVersionsByCapacityProviderRequest(TypedDict, closed=True):
    capacity_provider_name: (
        "capo_lambda.types.capacity_provider_name.CapacityProviderName"
    )
    """<p>The name of the capacity provider to list function versions for.</p>"""
    marker: NotRequired["capo_lambda.types.string.String"]
    """<p>Specify the pagination token that's returned by a previous request to retrieve the next page of results.</p>"""
    max_items: NotRequired["capo_lambda.types.max_fifty_list_items.MaxFiftyListItems"]
    """<p>The maximum number of function versions to return in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFunctionVersionsByCapacityProviderRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListFunctionVersionsByCapacityProviderRequest:
    out: ListFunctionVersionsByCapacityProviderRequest = {}  # type: ignore[typeddict-item]
    return out
