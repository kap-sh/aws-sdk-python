"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#UpdateChannelRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.channel_mode
    import aws_sdk_chime_sdk_messaging.types.chime_arn
    import aws_sdk_chime_sdk_messaging.types.metadata
    import aws_sdk_chime_sdk_messaging.types.non_empty_resource_name


class UpdateChannelRequest(TypedDict):
    channel_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the channel.</p>"""
    name: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.non_empty_resource_name.NonEmptyResourceName"
    ]
    """<p>The name of the channel.</p>"""
    mode: NotRequired["aws_sdk_chime_sdk_messaging.types.channel_mode.ChannelMode"]
    """<p>The mode of the update request.</p>"""
    metadata: NotRequired["aws_sdk_chime_sdk_messaging.types.metadata.Metadata"]
    """<p>The metadata for the update request.</p>"""
    chime_bearer: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateChannelRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "mode" in value:
        import aws_sdk_chime_sdk_messaging.types.channel_mode

        out["Mode"] = aws_sdk_chime_sdk_messaging.types.channel_mode.serialize_json(
            value["mode"]
        )
    if "metadata" in value:
        out["Metadata"] = value["metadata"]
    return out


def deserialize_json(data: dict) -> UpdateChannelRequest:
    out: UpdateChannelRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Mode" in data:
        import aws_sdk_chime_sdk_messaging.types.channel_mode

        out["mode"] = aws_sdk_chime_sdk_messaging.types.channel_mode.deserialize_json(
            data["Mode"]
        )
    if "Metadata" in data:
        out["metadata"] = data["Metadata"]
    return out
