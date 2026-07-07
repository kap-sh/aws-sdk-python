"""Generated from Smithy shape ``com.amazonaws.tnb#ListSolNetworkOperationsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_tnb.types.ns_instance_id
    import aws_sdk_tnb.types.pagination_token


class ListSolNetworkOperationsInput(TypedDict, closed=True):
    ns_instance_id: NotRequired["aws_sdk_tnb.types.ns_instance_id.NsInstanceId"]
    """<p>Network instance id filter, to retrieve network operations associated to a network instance.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to include in the response.</p>"""
    next_token: NotRequired["aws_sdk_tnb.types.pagination_token.PaginationToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSolNetworkOperationsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSolNetworkOperationsInput:
    out: ListSolNetworkOperationsInput = {}  # type: ignore[typeddict-item]
    return out
