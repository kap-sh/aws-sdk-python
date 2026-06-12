"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#DescribeChannelBanResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.channel_ban


class DescribeChannelBanResponse(TypedDict):
    channel_ban: NotRequired["aws_sdk_chime_sdk_messaging.types.channel_ban.ChannelBan"]
    """<p>The details of the ban.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeChannelBanResponse) -> dict:
    out: dict = {}
    if "channel_ban" in value:
        import aws_sdk_chime_sdk_messaging.types.channel_ban

        out["ChannelBan"] = (
            aws_sdk_chime_sdk_messaging.types.channel_ban.serialize_json(
                value["channel_ban"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeChannelBanResponse:
    out: DescribeChannelBanResponse = {}  # type: ignore[typeddict-item]
    if "ChannelBan" in data:
        import aws_sdk_chime_sdk_messaging.types.channel_ban

        out["channel_ban"] = (
            aws_sdk_chime_sdk_messaging.types.channel_ban.deserialize_json(
                data["ChannelBan"]
            )
        )
    return out
