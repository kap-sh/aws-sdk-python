"""Generated from Smithy shape ``com.amazonaws.sesv2#GetDedicatedIpsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.max_items
    import aws_sdk_sesv2.types.next_token
    import aws_sdk_sesv2.types.pool_name


class GetDedicatedIpsRequest(TypedDict):
    pool_name: NotRequired["aws_sdk_sesv2.types.pool_name.PoolName"]
    """<p>The name of the IP pool that the dedicated IP address is associated with.</p>"""
    next_token: NotRequired["aws_sdk_sesv2.types.next_token.NextToken"]
    """<p>A token returned from a previous call to <code>GetDedicatedIps</code> to indicate the position of the dedicated IP pool in the list of IP pools.</p>"""
    page_size: NotRequired["aws_sdk_sesv2.types.max_items.MaxItems"]
    """<p>The number of results to show in a single call to <code>GetDedicatedIpsRequest</code>. If the number of results is larger than the number you specified in this parameter, then the response includes a <code>NextToken</code> element, which you can use to obtain additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDedicatedIpsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDedicatedIpsRequest:
    out: GetDedicatedIpsRequest = {}  # type: ignore[typeddict-item]
    return out
