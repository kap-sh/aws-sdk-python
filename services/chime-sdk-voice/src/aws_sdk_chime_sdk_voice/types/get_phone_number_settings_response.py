"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#GetPhoneNumberSettingsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.calling_name
    import aws_sdk_chime_sdk_voice.types.iso8601_timestamp


class GetPhoneNumberSettingsResponse(TypedDict):
    calling_name: NotRequired["aws_sdk_chime_sdk_voice.types.calling_name.CallingName"]
    """<p>The default outbound calling name for the account.</p>"""
    calling_name_updated_timestamp: NotRequired[
        "aws_sdk_chime_sdk_voice.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The updated outbound calling name timestamp, in ISO 8601 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPhoneNumberSettingsResponse) -> dict:
    out: dict = {}
    if "calling_name" in value:
        out["CallingName"] = value["calling_name"]
    if "calling_name_updated_timestamp" in value:
        import aws_sdk_chime_sdk_voice.types.iso8601_timestamp

        out["CallingNameUpdatedTimestamp"] = (
            aws_sdk_chime_sdk_voice.types.iso8601_timestamp.serialize_json(
                value["calling_name_updated_timestamp"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetPhoneNumberSettingsResponse:
    out: GetPhoneNumberSettingsResponse = {}  # type: ignore[typeddict-item]
    if "CallingName" in data:
        out["calling_name"] = data["CallingName"]
    if "CallingNameUpdatedTimestamp" in data:
        import aws_sdk_chime_sdk_voice.types.iso8601_timestamp

        out["calling_name_updated_timestamp"] = (
            aws_sdk_chime_sdk_voice.types.iso8601_timestamp.deserialize_json(
                data["CallingNameUpdatedTimestamp"]
            )
        )
    return out
