"""Generated from Smithy shape ``com.amazonaws.connect#SearchEmailAddressesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.approximate_total_count
    import aws_sdk_connect.types.email_address_list
    import aws_sdk_connect.types.next_token


class SearchEmailAddressesResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""
    email_addresses: NotRequired[
        "aws_sdk_connect.types.email_address_list.EmailAddressList"
    ]
    """<p>List of email addresses matching SearchFilter and SearchCriteria </p>"""
    approximate_total_count: NotRequired[
        "aws_sdk_connect.types.approximate_total_count.ApproximateTotalCount"
    ]
    """<p>The total number of email addresses which matched your search query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchEmailAddressesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "email_addresses" in value:
        import aws_sdk_connect.types.email_address_list

        out["EmailAddresses"] = aws_sdk_connect.types.email_address_list.serialize_json(
            value["email_addresses"]
        )
    if "approximate_total_count" in value:
        out["ApproximateTotalCount"] = value["approximate_total_count"]
    return out


def deserialize_json(data: dict) -> SearchEmailAddressesResponse:
    out: SearchEmailAddressesResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "EmailAddresses" in data:
        import aws_sdk_connect.types.email_address_list

        out["email_addresses"] = (
            aws_sdk_connect.types.email_address_list.deserialize_json(
                data["EmailAddresses"]
            )
        )
    if "ApproximateTotalCount" in data:
        out["approximate_total_count"] = data["ApproximateTotalCount"]
    return out
