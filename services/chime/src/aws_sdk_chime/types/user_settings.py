"""Generated from Smithy shape ``com.amazonaws.chime#UserSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_chime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime.types.telephony_settings


class UserSettings(TypedDict, closed=True):
    telephony: "aws_sdk_chime.types.telephony_settings.TelephonySettings"
    """<p>The telephony settings associated with the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserSettings) -> dict:
    out: dict = {}
    import aws_sdk_chime.types.telephony_settings

    out["Telephony"] = aws_sdk_chime.types.telephony_settings.serialize_json(
        value["telephony"]
    )
    return out


def deserialize_json(data: dict) -> UserSettings:
    out: UserSettings = {}  # type: ignore[typeddict-item]
    if "Telephony" in data:
        import aws_sdk_chime.types.telephony_settings

        out["telephony"] = aws_sdk_chime.types.telephony_settings.deserialize_json(
            data["Telephony"]
        )
    else:
        raise DeserializationError("UserSettings.telephony required")
    return out
