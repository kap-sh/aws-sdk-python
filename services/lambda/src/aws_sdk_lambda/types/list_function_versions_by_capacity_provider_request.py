"""Generated from Smithy shape ``com.amazonaws.lambda#ListFunctionVersionsByCapacityProviderRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.capacity_provider_name
    import aws_sdk_lambda.types.max_fifty_list_items
    import aws_sdk_lambda.types.string


class ListFunctionVersionsByCapacityProviderRequest(TypedDict):
    capacity_provider_name: (
        "aws_sdk_lambda.types.capacity_provider_name.CapacityProviderName"
    )
    """<p>The name of the capacity provider to list function versions for.</p>"""
    marker: NotRequired["aws_sdk_lambda.types.string.String"]
    """<p>Specify the pagination token that's returned by a previous request to retrieve the next page of results.</p>"""
    max_items: NotRequired[
        "aws_sdk_lambda.types.max_fifty_list_items.MaxFiftyListItems"
    ]
    """<p>The maximum number of function versions to return in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFunctionVersionsByCapacityProviderRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListFunctionVersionsByCapacityProviderRequest:
    out: ListFunctionVersionsByCapacityProviderRequest = {}  # type: ignore[typeddict-item]
    return out
