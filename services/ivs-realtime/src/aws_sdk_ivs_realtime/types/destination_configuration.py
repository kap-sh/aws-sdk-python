"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#DestinationConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.channel_destination_configuration
    import aws_sdk_ivs_realtime.types.destination_configuration_name
    import aws_sdk_ivs_realtime.types.s3_destination_configuration


class DestinationConfiguration(TypedDict):
    name: NotRequired[
        "aws_sdk_ivs_realtime.types.destination_configuration_name.DestinationConfigurationName"
    ]
    """<p>Name that can be specified to help identify the destination.</p>"""
    channel: NotRequired[
        "aws_sdk_ivs_realtime.types.channel_destination_configuration.ChannelDestinationConfiguration"
    ]
    """<p>An IVS channel to be used for broadcasting, for server-side composition. Either a <code>channel</code> or an <code>s3</code> must be specified. </p>"""
    s3: NotRequired[
        "aws_sdk_ivs_realtime.types.s3_destination_configuration.S3DestinationConfiguration"
    ]
    """<p>An S3 storage configuration to be used for recording video data. Either a <code>channel</code> or an <code>s3</code> must be specified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DestinationConfiguration) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "channel" in value:
        import aws_sdk_ivs_realtime.types.channel_destination_configuration

        out["channel"] = (
            aws_sdk_ivs_realtime.types.channel_destination_configuration.serialize_json(
                value["channel"]
            )
        )
    if "s3" in value:
        import aws_sdk_ivs_realtime.types.s3_destination_configuration

        out["s3"] = (
            aws_sdk_ivs_realtime.types.s3_destination_configuration.serialize_json(
                value["s3"]
            )
        )
    return out


def deserialize_json(data: dict) -> DestinationConfiguration:
    out: DestinationConfiguration = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "channel" in data:
        import aws_sdk_ivs_realtime.types.channel_destination_configuration

        out["channel"] = (
            aws_sdk_ivs_realtime.types.channel_destination_configuration.deserialize_json(
                data["channel"]
            )
        )
    if "s3" in data:
        import aws_sdk_ivs_realtime.types.s3_destination_configuration

        out["s3"] = (
            aws_sdk_ivs_realtime.types.s3_destination_configuration.deserialize_json(
                data["s3"]
            )
        )
    return out
