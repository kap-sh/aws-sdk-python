"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelBanSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.identity


class ChannelBanSummary(TypedDict, closed=True):
    member: NotRequired["capo_chime_sdk_messaging.types.identity.Identity"]
    """<p>The member being banned from a channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelBanSummary) -> dict:
    out: dict = {}
    if "member" in value:
        import capo_chime_sdk_messaging.types.identity

        out["Member"] = capo_chime_sdk_messaging.types.identity.serialize_json(
            value["member"]
        )
    return out


def deserialize_json(data: dict) -> ChannelBanSummary:
    out: ChannelBanSummary = {}  # type: ignore[typeddict-item]
    if "Member" in data:
        import capo_chime_sdk_messaging.types.identity

        out["member"] = capo_chime_sdk_messaging.types.identity.deserialize_json(
            data["Member"]
        )
    return out
