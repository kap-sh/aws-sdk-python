"""Generated from Smithy shape ``com.amazonaws.securitylake#ListSubscribersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securitylake.types.next_token
    import capo_securitylake.types.subscriber_resource_list


class ListSubscribersResponse(TypedDict, closed=True):
    subscribers: NotRequired[
        "capo_securitylake.types.subscriber_resource_list.SubscriberResourceList"
    ]
    """<p>The subscribers available for the specified Security Lake account ID.</p>"""
    next_token: NotRequired["capo_securitylake.types.next_token.NextToken"]
    """<p>If nextToken is returned, there are more results available. You can repeat the call using the returned token to retrieve the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSubscribersResponse) -> dict:
    out: dict = {}
    if "subscribers" in value:
        import capo_securitylake.types.subscriber_resource_list

        out["subscribers"] = (
            capo_securitylake.types.subscriber_resource_list.serialize_json(
                value["subscribers"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSubscribersResponse:
    out: ListSubscribersResponse = {}  # type: ignore[typeddict-item]
    if "subscribers" in data:
        import capo_securitylake.types.subscriber_resource_list

        out["subscribers"] = (
            capo_securitylake.types.subscriber_resource_list.deserialize_json(
                data["subscribers"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
