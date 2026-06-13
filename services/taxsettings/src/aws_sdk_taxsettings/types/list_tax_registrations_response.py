"""Generated from Smithy shape ``com.amazonaws.taxsettings#ListTaxRegistrationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_taxsettings.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.account_details_list
    import aws_sdk_taxsettings.types.pagination_token_string


class ListTaxRegistrationsResponse(TypedDict):
    account_details: "aws_sdk_taxsettings.types.account_details_list.AccountDetailsList"
    """<p>The list of account details. This contains account Ids and TRN Information for each of the linked accounts. </p>"""
    next_token: NotRequired[
        "aws_sdk_taxsettings.types.pagination_token_string.PaginationTokenString"
    ]
    """<p> The token to retrieve the next set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTaxRegistrationsResponse) -> dict:
    out: dict = {}
    import aws_sdk_taxsettings.types.account_details_list

    out["accountDetails"] = (
        aws_sdk_taxsettings.types.account_details_list.serialize_json(
            value["account_details"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTaxRegistrationsResponse:
    out: ListTaxRegistrationsResponse = {}  # type: ignore[typeddict-item]
    if "accountDetails" in data:
        import aws_sdk_taxsettings.types.account_details_list

        out["account_details"] = (
            aws_sdk_taxsettings.types.account_details_list.deserialize_json(
                data["accountDetails"]
            )
        )
    else:
        raise DeserializationError(
            "ListTaxRegistrationsResponse.account_details required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
