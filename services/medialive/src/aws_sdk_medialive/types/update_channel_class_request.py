"""Generated from Smithy shape ``com.amazonaws.medialive#UpdateChannelClassRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_output_destination
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.channel_class


class UpdateChannelClassRequest(TypedDict, closed=True):
    channel_class: NotRequired["aws_sdk_medialive.types.channel_class.ChannelClass"]
    """The channel class that you wish to update this channel to use."""
    channel_id: "aws_sdk_medialive.types.__string.__string"
    """Channel Id of the channel whose class should be updated."""
    destinations: NotRequired[
        "aws_sdk_medialive.types.__list_of_output_destination.__listOfOutputDestination"
    ]
    """A list of output destinations for this channel."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateChannelClassRequest) -> dict:
    out: dict = {}
    if "channel_class" in value:
        import aws_sdk_medialive.types.channel_class

        out["channelClass"] = aws_sdk_medialive.types.channel_class.serialize_json(
            value["channel_class"]
        )
    if "destinations" in value:
        import aws_sdk_medialive.types.__list_of_output_destination

        out["destinations"] = (
            aws_sdk_medialive.types.__list_of_output_destination.serialize_json(
                value["destinations"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateChannelClassRequest:
    out: UpdateChannelClassRequest = {}  # type: ignore[typeddict-item]
    if "channelClass" in data:
        import aws_sdk_medialive.types.channel_class

        out["channel_class"] = aws_sdk_medialive.types.channel_class.deserialize_json(
            data["channelClass"]
        )
    if "destinations" in data:
        import aws_sdk_medialive.types.__list_of_output_destination

        out["destinations"] = (
            aws_sdk_medialive.types.__list_of_output_destination.deserialize_json(
                data["destinations"]
            )
        )
    return out
