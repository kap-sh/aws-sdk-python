"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#ListPartnersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_account.types.next_token
    import capo_partnercentral_account.types.partner_summary_list


class ListPartnersResponse(TypedDict, closed=True):
    partner_summary_list: (
        "capo_partnercentral_account.types.partner_summary_list.PartnerSummaryList"
    )
    """<p>A list of partner summaries including basic information about each partner account.</p>"""
    next_token: NotRequired["capo_partnercentral_account.types.next_token.NextToken"]
    """<p>The token for retrieving the next page of results if more results are available.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListPartnersResponse) -> dict:
    out: dict = {}
    import capo_partnercentral_account.types.partner_summary_list

    out["PartnerSummaryList"] = (
        capo_partnercentral_account.types.partner_summary_list.serialize_aws_json_1_0(
            value["partner_summary_list"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListPartnersResponse:
    out: ListPartnersResponse = {}  # type: ignore[typeddict-item]
    if "PartnerSummaryList" in data:
        import capo_partnercentral_account.types.partner_summary_list

        out["partner_summary_list"] = (
            capo_partnercentral_account.types.partner_summary_list.deserialize_aws_json_1_0(
                data["PartnerSummaryList"]
            )
        )
    else:
        raise DeserializationError("ListPartnersResponse.partner_summary_list required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
