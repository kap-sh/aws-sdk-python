"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#Channel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.channel_mode
    import capo_chime_sdk_messaging.types.channel_privacy
    import capo_chime_sdk_messaging.types.chime_arn
    import capo_chime_sdk_messaging.types.elastic_channel_configuration
    import capo_chime_sdk_messaging.types.expiration_settings
    import capo_chime_sdk_messaging.types.identity
    import capo_chime_sdk_messaging.types.metadata
    import capo_chime_sdk_messaging.types.non_empty_resource_name
    import capo_chime_sdk_messaging.types.timestamp


class Channel(TypedDict, closed=True):
    name: NotRequired[
        "capo_chime_sdk_messaging.types.non_empty_resource_name.NonEmptyResourceName"
    ]
    """<p>The name of a channel.</p>"""
    channel_arn: NotRequired["capo_chime_sdk_messaging.types.chime_arn.ChimeArn"]
    """<p>The ARN of a channel.</p>"""
    mode: NotRequired["capo_chime_sdk_messaging.types.channel_mode.ChannelMode"]
    """<p>The mode of the channel.</p>"""
    privacy: NotRequired[
        "capo_chime_sdk_messaging.types.channel_privacy.ChannelPrivacy"
    ]
    """<p>The channel's privacy setting.</p>"""
    metadata: NotRequired["capo_chime_sdk_messaging.types.metadata.Metadata"]
    """<p>The channel's metadata.</p>"""
    created_by: NotRequired["capo_chime_sdk_messaging.types.identity.Identity"]
    """<p>The <code>AppInstanceUser</code> who created the channel.</p>"""
    created_timestamp: NotRequired["capo_chime_sdk_messaging.types.timestamp.Timestamp"]
    """<p>The time at which the <code>AppInstanceUser</code> created the channel.</p>"""
    last_message_timestamp: NotRequired[
        "capo_chime_sdk_messaging.types.timestamp.Timestamp"
    ]
    """<p>The time at which a member sent the last message in the channel.</p>"""
    last_updated_timestamp: NotRequired[
        "capo_chime_sdk_messaging.types.timestamp.Timestamp"
    ]
    """<p>The time at which a channel was last updated.</p>"""
    channel_flow_arn: NotRequired["capo_chime_sdk_messaging.types.chime_arn.ChimeArn"]
    """<p>The ARN of the channel flow.</p>"""
    elastic_channel_configuration: NotRequired[
        "capo_chime_sdk_messaging.types.elastic_channel_configuration.ElasticChannelConfiguration"
    ]
    """<p>The attributes required to configure and create an elastic channel. An elastic channel can support a maximum of 1-million members.</p>"""
    expiration_settings: NotRequired[
        "capo_chime_sdk_messaging.types.expiration_settings.ExpirationSettings"
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
        import capo_chime_sdk_messaging.types.channel_mode

        out["Mode"] = capo_chime_sdk_messaging.types.channel_mode.serialize_json(
            value["mode"]
        )
    if "privacy" in value:
        import capo_chime_sdk_messaging.types.channel_privacy

        out["Privacy"] = capo_chime_sdk_messaging.types.channel_privacy.serialize_json(
            value["privacy"]
        )
    if "metadata" in value:
        out["Metadata"] = value["metadata"]
    if "created_by" in value:
        import capo_chime_sdk_messaging.types.identity

        out["CreatedBy"] = capo_chime_sdk_messaging.types.identity.serialize_json(
            value["created_by"]
        )
    if "created_timestamp" in value:
        import capo_chime_sdk_messaging.types.timestamp

        out["CreatedTimestamp"] = (
            capo_chime_sdk_messaging.types.timestamp.serialize_json(
                value["created_timestamp"]
            )
        )
    if "last_message_timestamp" in value:
        import capo_chime_sdk_messaging.types.timestamp

        out["LastMessageTimestamp"] = (
            capo_chime_sdk_messaging.types.timestamp.serialize_json(
                value["last_message_timestamp"]
            )
        )
    if "last_updated_timestamp" in value:
        import capo_chime_sdk_messaging.types.timestamp

        out["LastUpdatedTimestamp"] = (
            capo_chime_sdk_messaging.types.timestamp.serialize_json(
                value["last_updated_timestamp"]
            )
        )
    if "channel_flow_arn" in value:
        out["ChannelFlowArn"] = value["channel_flow_arn"]
    if "elastic_channel_configuration" in value:
        import capo_chime_sdk_messaging.types.elastic_channel_configuration

        out["ElasticChannelConfiguration"] = (
            capo_chime_sdk_messaging.types.elastic_channel_configuration.serialize_json(
                value["elastic_channel_configuration"]
            )
        )
    if "expiration_settings" in value:
        import capo_chime_sdk_messaging.types.expiration_settings

        out["ExpirationSettings"] = (
            capo_chime_sdk_messaging.types.expiration_settings.serialize_json(
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
        import capo_chime_sdk_messaging.types.channel_mode

        out["mode"] = capo_chime_sdk_messaging.types.channel_mode.deserialize_json(
            data["Mode"]
        )
    if "Privacy" in data:
        import capo_chime_sdk_messaging.types.channel_privacy

        out["privacy"] = (
            capo_chime_sdk_messaging.types.channel_privacy.deserialize_json(
                data["Privacy"]
            )
        )
    if "Metadata" in data:
        out["metadata"] = data["Metadata"]
    if "CreatedBy" in data:
        import capo_chime_sdk_messaging.types.identity

        out["created_by"] = capo_chime_sdk_messaging.types.identity.deserialize_json(
            data["CreatedBy"]
        )
    if "CreatedTimestamp" in data:
        import capo_chime_sdk_messaging.types.timestamp

        out["created_timestamp"] = (
            capo_chime_sdk_messaging.types.timestamp.deserialize_json(
                data["CreatedTimestamp"]
            )
        )
    if "LastMessageTimestamp" in data:
        import capo_chime_sdk_messaging.types.timestamp

        out["last_message_timestamp"] = (
            capo_chime_sdk_messaging.types.timestamp.deserialize_json(
                data["LastMessageTimestamp"]
            )
        )
    if "LastUpdatedTimestamp" in data:
        import capo_chime_sdk_messaging.types.timestamp

        out["last_updated_timestamp"] = (
            capo_chime_sdk_messaging.types.timestamp.deserialize_json(
                data["LastUpdatedTimestamp"]
            )
        )
    if "ChannelFlowArn" in data:
        out["channel_flow_arn"] = data["ChannelFlowArn"]
    if "ElasticChannelConfiguration" in data:
        import capo_chime_sdk_messaging.types.elastic_channel_configuration

        out["elastic_channel_configuration"] = (
            capo_chime_sdk_messaging.types.elastic_channel_configuration.deserialize_json(
                data["ElasticChannelConfiguration"]
            )
        )
    if "ExpirationSettings" in data:
        import capo_chime_sdk_messaging.types.expiration_settings

        out["expiration_settings"] = (
            capo_chime_sdk_messaging.types.expiration_settings.deserialize_json(
                data["ExpirationSettings"]
            )
        )
    return out
