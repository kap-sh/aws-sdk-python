"""Generated from Smithy shape ``com.amazonaws.pinpointemail#ListDedicatedIpPoolsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_email.types.list_of_dedicated_ip_pools
    import capo_pinpoint_email.types.next_token


class ListDedicatedIpPoolsResponse(TypedDict, closed=True):
    dedicated_ip_pools: NotRequired[
        "capo_pinpoint_email.types.list_of_dedicated_ip_pools.ListOfDedicatedIpPools"
    ]
    """<p>A list of all of the dedicated IP pools that are associated with your Amazon Pinpoint account.</p>"""
    next_token: NotRequired["capo_pinpoint_email.types.next_token.NextToken"]
    """<p>A token that indicates that there are additional IP pools to list. To view additional IP pools, issue another request to <code>ListDedicatedIpPools</code>, passing this token in the <code>NextToken</code> parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDedicatedIpPoolsResponse) -> dict:
    out: dict = {}
    if "dedicated_ip_pools" in value:
        import capo_pinpoint_email.types.list_of_dedicated_ip_pools

        out["DedicatedIpPools"] = (
            capo_pinpoint_email.types.list_of_dedicated_ip_pools.serialize_json(
                value["dedicated_ip_pools"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDedicatedIpPoolsResponse:
    out: ListDedicatedIpPoolsResponse = {}  # type: ignore[typeddict-item]
    if "DedicatedIpPools" in data:
        import capo_pinpoint_email.types.list_of_dedicated_ip_pools

        out["dedicated_ip_pools"] = (
            capo_pinpoint_email.types.list_of_dedicated_ip_pools.deserialize_json(
                data["DedicatedIpPools"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
