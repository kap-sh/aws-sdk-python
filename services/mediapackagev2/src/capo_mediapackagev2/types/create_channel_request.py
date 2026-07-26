"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#CreateChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mediapackagev2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediapackagev2.types.idempotency_token
    import capo_mediapackagev2.types.input_switch_configuration
    import capo_mediapackagev2.types.input_type
    import capo_mediapackagev2.types.output_header_configuration
    import capo_mediapackagev2.types.resource_description
    import capo_mediapackagev2.types.resource_name
    import capo_mediapackagev2.types.tag_map


class CreateChannelRequest(TypedDict, closed=True):
    channel_group_name: "capo_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.</p>"""
    channel_name: "capo_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. You can't change the name after you create the channel.</p>"""
    client_token: NotRequired[
        "capo_mediapackagev2.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive token that you provide to ensure the idempotency of the request.</p>"""
    input_type: NotRequired["capo_mediapackagev2.types.input_type.InputType"]
    """<p>The input type will be an immutable field which will be used to define whether the channel will allow CMAF ingest or HLS ingest. If unprovided, it will default to HLS to preserve current behavior.</p> <p>The allowed values are:</p> <ul> <li> <p> <code>HLS</code> - The HLS streaming specification (which defines M3U8 manifests and TS segments).</p> </li> <li> <p> <code>CMAF</code> - The DASH-IF CMAF Ingest specification (which defines CMAF segments with optional DASH manifests).</p> </li> </ul>"""
    description: NotRequired[
        "capo_mediapackagev2.types.resource_description.ResourceDescription"
    ]
    """<p>Enter any descriptive text that helps you to identify the channel.</p>"""
    input_switch_configuration: NotRequired[
        "capo_mediapackagev2.types.input_switch_configuration.InputSwitchConfiguration"
    ]
    """<p>The configuration for input switching based on the media quality confidence score (MQCS) as provided from AWS Elemental MediaLive. This setting is valid only when <code>InputType</code> is <code>CMAF</code>.</p>"""
    output_header_configuration: NotRequired[
        "capo_mediapackagev2.types.output_header_configuration.OutputHeaderConfiguration"
    ]
    """<p>The settings for what common media server data (CMSD) headers AWS Elemental MediaPackage includes in responses to the CDN. This setting is valid only when <code>InputType</code> is <code>CMAF</code>.</p>"""
    tags: NotRequired["capo_mediapackagev2.types.tag_map.TagMap"]
    r"""<p>A comma-separated list of tag key:value pairs that you define. For example:</p> <p> <code>\"Key1\": \"Value1\",</code> </p> <p> <code>\"Key2\": \"Value2\"</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateChannelRequest) -> dict:
    out: dict = {}
    out["ChannelName"] = value["channel_name"]
    if "input_type" in value:
        import capo_mediapackagev2.types.input_type

        out["InputType"] = capo_mediapackagev2.types.input_type.serialize_json(
            value["input_type"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "input_switch_configuration" in value:
        import capo_mediapackagev2.types.input_switch_configuration

        out["InputSwitchConfiguration"] = (
            capo_mediapackagev2.types.input_switch_configuration.serialize_json(
                value["input_switch_configuration"]
            )
        )
    if "output_header_configuration" in value:
        import capo_mediapackagev2.types.output_header_configuration

        out["OutputHeaderConfiguration"] = (
            capo_mediapackagev2.types.output_header_configuration.serialize_json(
                value["output_header_configuration"]
            )
        )
    if "tags" in value:
        import capo_mediapackagev2.types.tag_map

        out["tags"] = capo_mediapackagev2.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateChannelRequest:
    out: CreateChannelRequest = {}  # type: ignore[typeddict-item]
    if "ChannelName" in data:
        out["channel_name"] = data["ChannelName"]
    else:
        raise DeserializationError("CreateChannelRequest.channel_name required")
    if "InputType" in data:
        import capo_mediapackagev2.types.input_type

        out["input_type"] = capo_mediapackagev2.types.input_type.deserialize_json(
            data["InputType"]
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "InputSwitchConfiguration" in data:
        import capo_mediapackagev2.types.input_switch_configuration

        out["input_switch_configuration"] = (
            capo_mediapackagev2.types.input_switch_configuration.deserialize_json(
                data["InputSwitchConfiguration"]
            )
        )
    if "OutputHeaderConfiguration" in data:
        import capo_mediapackagev2.types.output_header_configuration

        out["output_header_configuration"] = (
            capo_mediapackagev2.types.output_header_configuration.deserialize_json(
                data["OutputHeaderConfiguration"]
            )
        )
    if "tags" in data:
        import capo_mediapackagev2.types.tag_map

        out["tags"] = capo_mediapackagev2.types.tag_map.deserialize_json(data["tags"])
    return out
