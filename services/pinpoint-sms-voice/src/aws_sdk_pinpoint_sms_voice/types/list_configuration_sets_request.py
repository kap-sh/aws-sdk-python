"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoice#ListConfigurationSetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice.types.__string


class ListConfigurationSetsRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_pinpoint_sms_voice.types.__string.__string"]
    """A token returned from a previous call to the API that indicates the position in the list of results."""
    page_size: NotRequired["aws_sdk_pinpoint_sms_voice.types.__string.__string"]
    """Used to specify the number of items that should be returned in the response."""


# --- restJson1 ser/de ---
def serialize_json(value: ListConfigurationSetsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListConfigurationSetsRequest:
    out: ListConfigurationSetsRequest = {}  # type: ignore[typeddict-item]
    return out
