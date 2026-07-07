"""Generated from Smithy shape ``com.amazonaws.connect#DescribePhoneNumberResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.claimed_phone_number_summary


class DescribePhoneNumberResponse(TypedDict, closed=True):
    claimed_phone_number_summary: NotRequired[
        "aws_sdk_connect.types.claimed_phone_number_summary.ClaimedPhoneNumberSummary"
    ]
    """<p>Information about a phone number that's been claimed to your Connect Customer instance or traffic distribution group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribePhoneNumberResponse) -> dict:
    out: dict = {}
    if "claimed_phone_number_summary" in value:
        import aws_sdk_connect.types.claimed_phone_number_summary

        out["ClaimedPhoneNumberSummary"] = (
            aws_sdk_connect.types.claimed_phone_number_summary.serialize_json(
                value["claimed_phone_number_summary"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribePhoneNumberResponse:
    out: DescribePhoneNumberResponse = {}  # type: ignore[typeddict-item]
    if "ClaimedPhoneNumberSummary" in data:
        import aws_sdk_connect.types.claimed_phone_number_summary

        out["claimed_phone_number_summary"] = (
            aws_sdk_connect.types.claimed_phone_number_summary.deserialize_json(
                data["ClaimedPhoneNumberSummary"]
            )
        )
    return out
