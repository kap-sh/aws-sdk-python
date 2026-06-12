"""Generated from Smithy shape ``com.amazonaws.connect#ListPhoneNumbersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.next_token
    import aws_sdk_connect.types.phone_number_summary_list


class ListPhoneNumbersResponse(TypedDict):
    phone_number_summary_list: NotRequired[
        "aws_sdk_connect.types.phone_number_summary_list.PhoneNumberSummaryList"
    ]
    """<p>Information about the phone numbers.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPhoneNumbersResponse) -> dict:
    out: dict = {}
    if "phone_number_summary_list" in value:
        import aws_sdk_connect.types.phone_number_summary_list

        out["PhoneNumberSummaryList"] = (
            aws_sdk_connect.types.phone_number_summary_list.serialize_json(
                value["phone_number_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPhoneNumbersResponse:
    out: ListPhoneNumbersResponse = {}  # type: ignore[typeddict-item]
    if "PhoneNumberSummaryList" in data:
        import aws_sdk_connect.types.phone_number_summary_list

        out["phone_number_summary_list"] = (
            aws_sdk_connect.types.phone_number_summary_list.deserialize_json(
                data["PhoneNumberSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
