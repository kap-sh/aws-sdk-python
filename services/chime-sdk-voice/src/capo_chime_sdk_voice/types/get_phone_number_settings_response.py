"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#GetPhoneNumberSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.calling_name
    import capo_chime_sdk_voice.types.iso8601_timestamp


class GetPhoneNumberSettingsResponse(TypedDict, closed=True):
    calling_name: NotRequired["capo_chime_sdk_voice.types.calling_name.CallingName"]
    """<p>The default outbound calling name for the account.</p>"""
    calling_name_updated_timestamp: NotRequired[
        "capo_chime_sdk_voice.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The updated outbound calling name timestamp, in ISO 8601 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPhoneNumberSettingsResponse) -> dict:
    out: dict = {}
    if "calling_name" in value:
        out["CallingName"] = value["calling_name"]
    if "calling_name_updated_timestamp" in value:
        import capo_chime_sdk_voice.types.iso8601_timestamp

        out["CallingNameUpdatedTimestamp"] = (
            capo_chime_sdk_voice.types.iso8601_timestamp.serialize_json(
                value["calling_name_updated_timestamp"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetPhoneNumberSettingsResponse:
    out: GetPhoneNumberSettingsResponse = {}  # type: ignore[typeddict-item]
    if "CallingName" in data:
        out["calling_name"] = data["CallingName"]
    if "CallingNameUpdatedTimestamp" in data:
        import capo_chime_sdk_voice.types.iso8601_timestamp

        out["calling_name_updated_timestamp"] = (
            capo_chime_sdk_voice.types.iso8601_timestamp.deserialize_json(
                data["CallingNameUpdatedTimestamp"]
            )
        )
    return out
