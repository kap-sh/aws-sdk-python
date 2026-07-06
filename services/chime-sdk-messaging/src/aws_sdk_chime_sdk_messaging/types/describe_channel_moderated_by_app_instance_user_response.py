"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#DescribeChannelModeratedByAppInstanceUserResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.channel_moderated_by_app_instance_user_summary


class DescribeChannelModeratedByAppInstanceUserResponse(TypedDict, closed=True):
    channel: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.channel_moderated_by_app_instance_user_summary.ChannelModeratedByAppInstanceUserSummary"
    ]
    """<p>The moderated channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeChannelModeratedByAppInstanceUserResponse) -> dict:
    out: dict = {}
    if "channel" in value:
        import aws_sdk_chime_sdk_messaging.types.channel_moderated_by_app_instance_user_summary

        out["Channel"] = (
            aws_sdk_chime_sdk_messaging.types.channel_moderated_by_app_instance_user_summary.serialize_json(
                value["channel"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeChannelModeratedByAppInstanceUserResponse:
    out: DescribeChannelModeratedByAppInstanceUserResponse = {}  # type: ignore[typeddict-item]
    if "Channel" in data:
        import aws_sdk_chime_sdk_messaging.types.channel_moderated_by_app_instance_user_summary

        out["channel"] = (
            aws_sdk_chime_sdk_messaging.types.channel_moderated_by_app_instance_user_summary.deserialize_json(
                data["Channel"]
            )
        )
    return out
