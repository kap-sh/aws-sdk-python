"""Generated from Smithy shape ``com.amazonaws.connect#ListPhoneNumbersV2Response``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.large_next_token
    import capo_connect.types.list_phone_numbers_summary_list


class ListPhoneNumbersV2Response(TypedDict, closed=True):
    next_token: NotRequired["capo_connect.types.large_next_token.LargeNextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""
    list_phone_numbers_summary_list: NotRequired[
        "capo_connect.types.list_phone_numbers_summary_list.ListPhoneNumbersSummaryList"
    ]
    """<p>Information about phone numbers that have been claimed to your Connect Customer instances or traffic distribution groups.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPhoneNumbersV2Response) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "list_phone_numbers_summary_list" in value:
        import capo_connect.types.list_phone_numbers_summary_list

        out["ListPhoneNumbersSummaryList"] = (
            capo_connect.types.list_phone_numbers_summary_list.serialize_json(
                value["list_phone_numbers_summary_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListPhoneNumbersV2Response:
    out: ListPhoneNumbersV2Response = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ListPhoneNumbersSummaryList" in data:
        import capo_connect.types.list_phone_numbers_summary_list

        out["list_phone_numbers_summary_list"] = (
            capo_connect.types.list_phone_numbers_summary_list.deserialize_json(
                data["ListPhoneNumbersSummaryList"]
            )
        )
    return out
