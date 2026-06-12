"""Generated from Smithy shape ``com.amazonaws.connect#SearchAvailablePhoneNumbersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.available_numbers_list
    import aws_sdk_connect.types.large_next_token


class SearchAvailablePhoneNumbersResponse(TypedDict):
    next_token: NotRequired["aws_sdk_connect.types.large_next_token.LargeNextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""
    available_numbers_list: NotRequired[
        "aws_sdk_connect.types.available_numbers_list.AvailableNumbersList"
    ]
    """<p>A list of available phone numbers that you can claim to your Connect Customer instance or traffic distribution group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchAvailablePhoneNumbersResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "available_numbers_list" in value:
        import aws_sdk_connect.types.available_numbers_list

        out["AvailableNumbersList"] = (
            aws_sdk_connect.types.available_numbers_list.serialize_json(
                value["available_numbers_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> SearchAvailablePhoneNumbersResponse:
    out: SearchAvailablePhoneNumbersResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "AvailableNumbersList" in data:
        import aws_sdk_connect.types.available_numbers_list

        out["available_numbers_list"] = (
            aws_sdk_connect.types.available_numbers_list.deserialize_json(
                data["AvailableNumbersList"]
            )
        )
    return out
