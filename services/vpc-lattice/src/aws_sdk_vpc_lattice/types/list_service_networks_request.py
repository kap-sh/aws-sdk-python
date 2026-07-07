"""Generated from Smithy shape ``com.amazonaws.vpclattice#ListServiceNetworksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.max_results
    import aws_sdk_vpc_lattice.types.next_token


class ListServiceNetworksRequest(TypedDict, closed=True):
    max_results: NotRequired["aws_sdk_vpc_lattice.types.max_results.MaxResults"]
    """<p>The maximum number of results to return.</p>"""
    next_token: NotRequired["aws_sdk_vpc_lattice.types.next_token.NextToken"]
    """<p>A pagination token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListServiceNetworksRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListServiceNetworksRequest:
    out: ListServiceNetworksRequest = {}  # type: ignore[typeddict-item]
    return out
