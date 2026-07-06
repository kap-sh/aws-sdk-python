"""Generated from Smithy shape ``com.amazonaws.vpclattice#ListListenersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.max_results
    import aws_sdk_vpc_lattice.types.next_token
    import aws_sdk_vpc_lattice.types.service_identifier


class ListListenersRequest(TypedDict, closed=True):
    service_identifier: "aws_sdk_vpc_lattice.types.service_identifier.ServiceIdentifier"
    """<p>The ID or ARN of the service.</p>"""
    max_results: NotRequired["aws_sdk_vpc_lattice.types.max_results.MaxResults"]
    """<p>The maximum number of results to return.</p>"""
    next_token: NotRequired["aws_sdk_vpc_lattice.types.next_token.NextToken"]
    """<p>A pagination token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListListenersRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListListenersRequest:
    out: ListListenersRequest = {}  # type: ignore[typeddict-item]
    return out
