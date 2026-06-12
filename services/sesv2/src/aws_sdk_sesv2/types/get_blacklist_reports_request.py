"""Generated from Smithy shape ``com.amazonaws.sesv2#GetBlacklistReportsRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.blacklist_item_names


class GetBlacklistReportsRequest(TypedDict):
    blacklist_item_names: "aws_sdk_sesv2.types.blacklist_item_names.BlacklistItemNames"
    """<p>A list of IP addresses that you want to retrieve blacklist information about. You can only specify the dedicated IP addresses that you use to send email using Amazon SES or Amazon Pinpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBlacklistReportsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetBlacklistReportsRequest:
    out: GetBlacklistReportsRequest = {}  # type: ignore[typeddict-item]
    return out
