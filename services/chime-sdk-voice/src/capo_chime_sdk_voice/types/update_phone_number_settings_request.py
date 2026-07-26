"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#UpdatePhoneNumberSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_chime_sdk_voice.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.calling_name


class UpdatePhoneNumberSettingsRequest(TypedDict, closed=True):
    calling_name: "capo_chime_sdk_voice.types.calling_name.CallingName"
    """<p>The default outbound calling name for the account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePhoneNumberSettingsRequest) -> dict:
    out: dict = {}
    out["CallingName"] = value["calling_name"]
    return out


def deserialize_json(data: dict) -> UpdatePhoneNumberSettingsRequest:
    out: UpdatePhoneNumberSettingsRequest = {}  # type: ignore[typeddict-item]
    if "CallingName" in data:
        out["calling_name"] = data["CallingName"]
    else:
        raise DeserializationError(
            "UpdatePhoneNumberSettingsRequest.calling_name required"
        )
    return out
