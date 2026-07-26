"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#CreateChannelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mediapackagev2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_mediapackagev2.types.entity_tag
    import capo_mediapackagev2.types.ingest_endpoint_list
    import capo_mediapackagev2.types.input_switch_configuration
    import capo_mediapackagev2.types.input_type
    import capo_mediapackagev2.types.output_header_configuration
    import capo_mediapackagev2.types.resource_description
    import capo_mediapackagev2.types.tag_map


class CreateChannelResponse(TypedDict, closed=True):
    arn: "str"
    """<p>The Amazon Resource Name (ARN) associated with the resource.</p>"""
    channel_name: "str"
    """<p>The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group.</p>"""
    channel_group_name: "str"
    """<p>The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time the channel was created.</p>"""
    modified_at: "datetime.datetime"
    """<p>The date and time the channel was modified.</p>"""
    description: NotRequired[
        "capo_mediapackagev2.types.resource_description.ResourceDescription"
    ]
    """<p>The description for your channel.</p>"""
    ingest_endpoints: NotRequired[
        "capo_mediapackagev2.types.ingest_endpoint_list.IngestEndpointList"
    ]
    input_type: NotRequired["capo_mediapackagev2.types.input_type.InputType"]
    """<p>The input type will be an immutable field which will be used to define whether the channel will allow CMAF ingest or HLS ingest. If unprovided, it will default to HLS to preserve current behavior.</p> <p>The allowed values are:</p> <ul> <li> <p> <code>HLS</code> - The HLS streaming specification (which defines M3U8 manifests and TS segments).</p> </li> <li> <p> <code>CMAF</code> - The DASH-IF CMAF Ingest specification (which defines CMAF segments with optional DASH manifests).</p> </li> </ul>"""
    e_tag: NotRequired["capo_mediapackagev2.types.entity_tag.EntityTag"]
    """<p>The current Entity Tag (ETag) associated with this resource. The entity tag can be used to safely make concurrent updates to the resource.</p>"""
    tags: NotRequired["capo_mediapackagev2.types.tag_map.TagMap"]
    """<p>The comma-separated list of tag key:value pairs assigned to the channel.</p>"""
    input_switch_configuration: NotRequired[
        "capo_mediapackagev2.types.input_switch_configuration.InputSwitchConfiguration"
    ]
    """<p>The configuration for input switching based on the media quality confidence score (MQCS) as provided from AWS Elemental MediaLive. This setting is valid only when <code>InputType</code> is <code>CMAF</code>.</p>"""
    output_header_configuration: NotRequired[
        "capo_mediapackagev2.types.output_header_configuration.OutputHeaderConfiguration"
    ]
    """<p>The settings for what common media server data (CMSD) headers AWS Elemental MediaPackage includes in responses to the CDN. This setting is valid only when <code>InputType</code> is <code>CMAF</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateChannelResponse) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["ChannelName"] = value["channel_name"]
    out["ChannelGroupName"] = value["channel_group_name"]
    import capo_mediapackagev2.types._prelude.timestamp

    out["CreatedAt"] = capo_mediapackagev2.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_mediapackagev2.types._prelude.timestamp

    out["ModifiedAt"] = capo_mediapackagev2.types._prelude.timestamp.serialize_json(
        value["modified_at"]
    )
    if "description" in value:
        out["Description"] = value["description"]
    if "ingest_endpoints" in value:
        import capo_mediapackagev2.types.ingest_endpoint_list

        out["IngestEndpoints"] = (
            capo_mediapackagev2.types.ingest_endpoint_list.serialize_json(
                value["ingest_endpoints"]
            )
        )
    if "input_type" in value:
        import capo_mediapackagev2.types.input_type

        out["InputType"] = capo_mediapackagev2.types.input_type.serialize_json(
            value["input_type"]
        )
    if "e_tag" in value:
        out["ETag"] = value["e_tag"]
    if "tags" in value:
        import capo_mediapackagev2.types.tag_map

        out["Tags"] = capo_mediapackagev2.types.tag_map.serialize_json(value["tags"])
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
    return out


def deserialize_json(data: dict) -> CreateChannelResponse:
    out: CreateChannelResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("CreateChannelResponse.arn required")
    if "ChannelName" in data:
        out["channel_name"] = data["ChannelName"]
    else:
        raise DeserializationError("CreateChannelResponse.channel_name required")
    if "ChannelGroupName" in data:
        out["channel_group_name"] = data["ChannelGroupName"]
    else:
        raise DeserializationError("CreateChannelResponse.channel_group_name required")
    if "CreatedAt" in data:
        import capo_mediapackagev2.types._prelude.timestamp

        out["created_at"] = (
            capo_mediapackagev2.types._prelude.timestamp.deserialize_json(
                data["CreatedAt"]
            )
        )
    else:
        raise DeserializationError("CreateChannelResponse.created_at required")
    if "ModifiedAt" in data:
        import capo_mediapackagev2.types._prelude.timestamp

        out["modified_at"] = (
            capo_mediapackagev2.types._prelude.timestamp.deserialize_json(
                data["ModifiedAt"]
            )
        )
    else:
        raise DeserializationError("CreateChannelResponse.modified_at required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "IngestEndpoints" in data:
        import capo_mediapackagev2.types.ingest_endpoint_list

        out["ingest_endpoints"] = (
            capo_mediapackagev2.types.ingest_endpoint_list.deserialize_json(
                data["IngestEndpoints"]
            )
        )
    if "InputType" in data:
        import capo_mediapackagev2.types.input_type

        out["input_type"] = capo_mediapackagev2.types.input_type.deserialize_json(
            data["InputType"]
        )
    if "ETag" in data:
        out["e_tag"] = data["ETag"]
    if "Tags" in data:
        import capo_mediapackagev2.types.tag_map

        out["tags"] = capo_mediapackagev2.types.tag_map.deserialize_json(data["Tags"])
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
    return out
