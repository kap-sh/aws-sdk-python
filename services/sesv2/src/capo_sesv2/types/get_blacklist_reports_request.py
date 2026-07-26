"""Generated from Smithy shape ``com.amazonaws.sesv2#GetBlacklistReportsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.blacklist_item_names


class GetBlacklistReportsRequest(TypedDict, closed=True):
    blacklist_item_names: "capo_sesv2.types.blacklist_item_names.BlacklistItemNames"
    """<p>A list of IP addresses that you want to retrieve blacklist information about. You can only specify the dedicated IP addresses that you use to send email using Amazon SES or Amazon Pinpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBlacklistReportsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetBlacklistReportsRequest:
    out: GetBlacklistReportsRequest = {}  # type: ignore[typeddict-item]
    return out
