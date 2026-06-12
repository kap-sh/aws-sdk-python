"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#Channel``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.channel_mode
    import aws_sdk_chime_sdk_messaging.types.channel_privacy
    import aws_sdk_chime_sdk_messaging.types.chime_arn
    import aws_sdk_chime_sdk_messaging.types.elastic_channel_configuration
    import aws_sdk_chime_sdk_messaging.types.expiration_settings
    import aws_sdk_chime_sdk_messaging.types.identity
    import aws_sdk_chime_sdk_messaging.types.metadata
    import aws_sdk_chime_sdk_messaging.types.non_empty_resource_name
    import aws_sdk_chime_sdk_messaging.types.timestamp


class Channel(TypedDict):
    name: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.non_empty_resource_name.NonEmptyResourceName"
    ]
    """<p>The name of a channel.</p>"""
    channel_arn: NotRequired["aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"]
    """<p>The ARN of a channel.</p>"""
    mode: NotRequired["aws_sdk_chime_sdk_messaging.types.channel_mode.ChannelMode"]
    """<p>The mode of the channel.</p>"""
    privacy: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.channel_privacy.ChannelPrivacy"
    ]
    """<p>The channel's privacy setting.</p>"""
    metadata: NotRequired["aws_sdk_chime_sdk_messaging.types.metadata.Metadata"]
    """<p>The channel's metadata.</p>"""
    created_by: NotRequired["aws_sdk_chime_sdk_messaging.types.identity.Identity"]
    """<p>The <code>AppInstanceUser</code> who created the channel.</p>"""
    created_timestamp: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.timestamp.Timestamp"
    ]
    """<p>The time at which the <code>AppInstanceUser</code> created the channel.</p>"""
    last_message_timestamp: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.timestamp.Timestamp"
    ]
    """<p>The time at which a member sent the last message in the channel.</p>"""
    last_updated_timestamp: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.timestamp.Timestamp"
    ]
    """<p>The time at which a channel was last updated.</p>"""
    channel_flow_arn: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
    ]
    """<p>The ARN of the channel flow.</p>"""
    elastic_channel_configuration: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.elastic_channel_configuration.ElasticChannelConfiguration"
    ]
    """<p>The attributes required to configure and create an elastic channel. An elastic channel can support a maximum of 1-million members.</p>"""
    expiration_settings: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.expiration_settings.ExpirationSettings"
    ]
    """<p>Settings that control when a channel expires.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Channel) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "channel_arn" in value:
        out["ChannelArn"] = value["channel_arn"]
    if "mode" in value:
        import aws_sdk_chime_sdk_messaging.types.channel_mode

        out["Mode"] = aws_sdk_chime_sdk_messaging.types.channel_mode.serialize_json(
            value["mode"]
        )
    if "privacy" in value:
        import aws_sdk_chime_sdk_messaging.types.channel_privacy

        out["Privacy"] = (
            aws_sdk_chime_sdk_messaging.types.channel_privacy.serialize_json(
                value["privacy"]
            )
        )
    if "metadata" in value:
        out["Metadata"] = value["metadata"]
    if "created_by" in value:
        import aws_sdk_chime_sdk_messaging.types.identity

        out["CreatedBy"] = aws_sdk_chime_sdk_messaging.types.identity.serialize_json(
            value["created_by"]
        )
    if "created_timestamp" in value:
        import aws_sdk_chime_sdk_messaging.types.timestamp

        out["CreatedTimestamp"] = (
            aws_sdk_chime_sdk_messaging.types.timestamp.serialize_json(
                value["created_timestamp"]
            )
        )
    if "last_message_timestamp" in value:
        import aws_sdk_chime_sdk_messaging.types.timestamp

        out["LastMessageTimestamp"] = (
            aws_sdk_chime_sdk_messaging.types.timestamp.serialize_json(
                value["last_message_timestamp"]
            )
        )
    if "last_updated_timestamp" in value:
        import aws_sdk_chime_sdk_messaging.types.timestamp

        out["LastUpdatedTimestamp"] = (
            aws_sdk_chime_sdk_messaging.types.timestamp.serialize_json(
                value["last_updated_timestamp"]
            )
        )
    if "channel_flow_arn" in value:
        out["ChannelFlowArn"] = value["channel_flow_arn"]
    if "elastic_channel_configuration" in value:
        import aws_sdk_chime_sdk_messaging.types.elastic_channel_configuration

        out["ElasticChannelConfiguration"] = (
            aws_sdk_chime_sdk_messaging.types.elastic_channel_configuration.serialize_json(
                value["elastic_channel_configuration"]
            )
        )
    if "expiration_settings" in value:
        import aws_sdk_chime_sdk_messaging.types.expiration_settings

        out["ExpirationSettings"] = (
            aws_sdk_chime_sdk_messaging.types.expiration_settings.serialize_json(
                value["expiration_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> Channel:
    out: Channel = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "ChannelArn" in data:
        out["channel_arn"] = data["ChannelArn"]
    if "Mode" in data:
        import aws_sdk_chime_sdk_messaging.types.channel_mode

        out["mode"] = aws_sdk_chime_sdk_messaging.types.channel_mode.deserialize_json(
            data["Mode"]
        )
    if "Privacy" in data:
        import aws_sdk_chime_sdk_messaging.types.channel_privacy

        out["privacy"] = (
            aws_sdk_chime_sdk_messaging.types.channel_privacy.deserialize_json(
                data["Privacy"]
            )
        )
    if "Metadata" in data:
        out["metadata"] = data["Metadata"]
    if "CreatedBy" in data:
        import aws_sdk_chime_sdk_messaging.types.identity

        out["created_by"] = aws_sdk_chime_sdk_messaging.types.identity.deserialize_json(
            data["CreatedBy"]
        )
    if "CreatedTimestamp" in data:
        import aws_sdk_chime_sdk_messaging.types.timestamp

        out["created_timestamp"] = (
            aws_sdk_chime_sdk_messaging.types.timestamp.deserialize_json(
                data["CreatedTimestamp"]
            )
        )
    if "LastMessageTimestamp" in data:
        import aws_sdk_chime_sdk_messaging.types.timestamp

        out["last_message_timestamp"] = (
            aws_sdk_chime_sdk_messaging.types.timestamp.deserialize_json(
                data["LastMessageTimestamp"]
            )
        )
    if "LastUpdatedTimestamp" in data:
        import aws_sdk_chime_sdk_messaging.types.timestamp

        out["last_updated_timestamp"] = (
            aws_sdk_chime_sdk_messaging.types.timestamp.deserialize_json(
                data["LastUpdatedTimestamp"]
            )
        )
    if "ChannelFlowArn" in data:
        out["channel_flow_arn"] = data["ChannelFlowArn"]
    if "ElasticChannelConfiguration" in data:
        import aws_sdk_chime_sdk_messaging.types.elastic_channel_configuration

        out["elastic_channel_configuration"] = (
            aws_sdk_chime_sdk_messaging.types.elastic_channel_configuration.deserialize_json(
                data["ElasticChannelConfiguration"]
            )
        )
    if "ExpirationSettings" in data:
        import aws_sdk_chime_sdk_messaging.types.expiration_settings

        out["expiration_settings"] = (
            aws_sdk_chime_sdk_messaging.types.expiration_settings.deserialize_json(
                data["ExpirationSettings"]
            )
        )
    return out
