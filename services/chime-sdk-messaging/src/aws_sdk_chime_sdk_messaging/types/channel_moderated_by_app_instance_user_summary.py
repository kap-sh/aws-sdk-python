"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelModeratedByAppInstanceUserSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.channel_summary


class ChannelModeratedByAppInstanceUserSummary(TypedDict, closed=True):
    channel_summary: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.channel_summary.ChannelSummary"
    ]
    """<p>Summary of the details of a <code>Channel</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelModeratedByAppInstanceUserSummary) -> dict:
    out: dict = {}
    if "channel_summary" in value:
        import aws_sdk_chime_sdk_messaging.types.channel_summary

        out["ChannelSummary"] = (
            aws_sdk_chime_sdk_messaging.types.channel_summary.serialize_json(
                value["channel_summary"]
            )
        )
    return out


def deserialize_json(data: dict) -> ChannelModeratedByAppInstanceUserSummary:
    out: ChannelModeratedByAppInstanceUserSummary = {}  # type: ignore[typeddict-item]
    if "ChannelSummary" in data:
        import aws_sdk_chime_sdk_messaging.types.channel_summary

        out["channel_summary"] = (
            aws_sdk_chime_sdk_messaging.types.channel_summary.deserialize_json(
                data["ChannelSummary"]
            )
        )
    return out
