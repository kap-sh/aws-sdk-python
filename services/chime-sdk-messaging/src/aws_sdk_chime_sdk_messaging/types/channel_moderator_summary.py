"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelModeratorSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.identity


class ChannelModeratorSummary(TypedDict):
    moderator: NotRequired["aws_sdk_chime_sdk_messaging.types.identity.Identity"]
    """<p>The data for a moderator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelModeratorSummary) -> dict:
    out: dict = {}
    if "moderator" in value:
        import aws_sdk_chime_sdk_messaging.types.identity

        out["Moderator"] = aws_sdk_chime_sdk_messaging.types.identity.serialize_json(
            value["moderator"]
        )
    return out


def deserialize_json(data: dict) -> ChannelModeratorSummary:
    out: ChannelModeratorSummary = {}  # type: ignore[typeddict-item]
    if "Moderator" in data:
        import aws_sdk_chime_sdk_messaging.types.identity

        out["moderator"] = aws_sdk_chime_sdk_messaging.types.identity.deserialize_json(
            data["Moderator"]
        )
    return out
