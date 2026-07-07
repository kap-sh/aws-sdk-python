"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ListEntitlementsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.__list_of_listed_entitlement


class ListEntitlementsResponse(TypedDict, closed=True):
    entitlements: NotRequired[
        "aws_sdk_mediaconnect.types.__list_of_listed_entitlement.__listOfListedEntitlement"
    ]
    """<p>A list of entitlements that have been granted to you from other Amazon Web Services accounts. </p>"""
    next_token: NotRequired["str"]
    """<p>The token that identifies the batch of results that you want to see. </p> <p>For example, you submit a ListEntitlements request with <code>MaxResults</code> set at 5. The service returns the first batch of results (up to 5) and a NextToken value. To see the next batch of results, you can submit the <code>ListEntitlements</code> request a second time and specify the <code>NextToken</code> value. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEntitlementsResponse) -> dict:
    out: dict = {}
    if "entitlements" in value:
        import aws_sdk_mediaconnect.types.__list_of_listed_entitlement

        out["entitlements"] = (
            aws_sdk_mediaconnect.types.__list_of_listed_entitlement.serialize_json(
                value["entitlements"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEntitlementsResponse:
    out: ListEntitlementsResponse = {}  # type: ignore[typeddict-item]
    if "entitlements" in data:
        import aws_sdk_mediaconnect.types.__list_of_listed_entitlement

        out["entitlements"] = (
            aws_sdk_mediaconnect.types.__list_of_listed_entitlement.deserialize_json(
                data["entitlements"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
