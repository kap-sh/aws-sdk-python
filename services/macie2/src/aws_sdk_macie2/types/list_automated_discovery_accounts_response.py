"""Generated from Smithy shape ``com.amazonaws.macie2#ListAutomatedDiscoveryAccountsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__list_of_automated_discovery_account
    import aws_sdk_macie2.types.__string


class ListAutomatedDiscoveryAccountsResponse(TypedDict):
    items: NotRequired[
        "aws_sdk_macie2.types.__list_of_automated_discovery_account.__listOfAutomatedDiscoveryAccount"
    ]
    """<p>An array of objects, one for each account specified in the request. Each object specifies the Amazon Web Services account ID for an account and the current status of automated sensitive data discovery for that account.</p>"""
    next_token: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAutomatedDiscoveryAccountsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_macie2.types.__list_of_automated_discovery_account

        out["items"] = (
            aws_sdk_macie2.types.__list_of_automated_discovery_account.serialize_json(
                value["items"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAutomatedDiscoveryAccountsResponse:
    out: ListAutomatedDiscoveryAccountsResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_macie2.types.__list_of_automated_discovery_account

        out["items"] = (
            aws_sdk_macie2.types.__list_of_automated_discovery_account.deserialize_json(
                data["items"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
