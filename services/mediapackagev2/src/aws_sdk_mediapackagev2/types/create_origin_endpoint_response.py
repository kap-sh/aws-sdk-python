"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#CreateOriginEndpointResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mediapackagev2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_mediapackagev2.types.container_type
    import aws_sdk_mediapackagev2.types.entity_tag
    import aws_sdk_mediapackagev2.types.force_endpoint_error_configuration
    import aws_sdk_mediapackagev2.types.get_dash_manifests
    import aws_sdk_mediapackagev2.types.get_hls_manifests
    import aws_sdk_mediapackagev2.types.get_low_latency_hls_manifests
    import aws_sdk_mediapackagev2.types.get_mss_manifests
    import aws_sdk_mediapackagev2.types.resource_description
    import aws_sdk_mediapackagev2.types.resource_name
    import aws_sdk_mediapackagev2.types.segment
    import aws_sdk_mediapackagev2.types.tag_map
    import aws_sdk_mediapackagev2.types.uri_separator


class CreateOriginEndpointResponse(TypedDict):
    arn: "str"
    """<p>The Amazon Resource Name (ARN) associated with the resource.</p>"""
    channel_group_name: "aws_sdk_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.</p>"""
    channel_name: "aws_sdk_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group.</p>"""
    origin_endpoint_name: "aws_sdk_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name that describes the origin endpoint. The name is the primary identifier for the origin endpoint, and and must be unique for your account in the AWS Region and channel.</p>"""
    container_type: "aws_sdk_mediapackagev2.types.container_type.ContainerType"
    """<p>The type of container attached to this origin endpoint.</p>"""
    segment: "aws_sdk_mediapackagev2.types.segment.Segment"
    """<p>The segment configuration, including the segment name, duration, and other configuration values.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time the origin endpoint was created.</p>"""
    modified_at: "datetime.datetime"
    """<p>The date and time the origin endpoint was modified.</p>"""
    description: NotRequired[
        "aws_sdk_mediapackagev2.types.resource_description.ResourceDescription"
    ]
    """<p>The description for your origin endpoint.</p>"""
    startover_window_seconds: NotRequired["int"]
    """<p>The size of the window (in seconds) to create a window of the live stream that's available for on-demand viewing. Viewers can start-over or catch-up on content that falls within the window.</p>"""
    hls_manifests: NotRequired[
        "aws_sdk_mediapackagev2.types.get_hls_manifests.GetHlsManifests"
    ]
    """<p>An HTTP live streaming (HLS) manifest configuration.</p>"""
    low_latency_hls_manifests: NotRequired[
        "aws_sdk_mediapackagev2.types.get_low_latency_hls_manifests.GetLowLatencyHlsManifests"
    ]
    """<p>A low-latency HLS manifest configuration.</p>"""
    dash_manifests: NotRequired[
        "aws_sdk_mediapackagev2.types.get_dash_manifests.GetDashManifests"
    ]
    """<p>A DASH manifest configuration.</p>"""
    mss_manifests: NotRequired[
        "aws_sdk_mediapackagev2.types.get_mss_manifests.GetMssManifests"
    ]
    """<p>The Microsoft Smooth Streaming (MSS) manifest configurations that were created for this origin endpoint.</p>"""
    force_endpoint_error_configuration: NotRequired[
        "aws_sdk_mediapackagev2.types.force_endpoint_error_configuration.ForceEndpointErrorConfiguration"
    ]
    """<p>The failover settings for the endpoint.</p>"""
    uri_separator: NotRequired[
        "aws_sdk_mediapackagev2.types.uri_separator.UriSeparator"
    ]
    """<p>The separator character used in generated URIs for this origin endpoint.</p>"""
    e_tag: NotRequired["aws_sdk_mediapackagev2.types.entity_tag.EntityTag"]
    """<p>The current Entity Tag (ETag) associated with this resource. The entity tag can be used to safely make concurrent updates to the resource.</p>"""
    tags: NotRequired["aws_sdk_mediapackagev2.types.tag_map.TagMap"]
    """<p>The comma-separated list of tag key:value pairs assigned to the origin endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateOriginEndpointResponse) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["ChannelGroupName"] = value["channel_group_name"]
    out["ChannelName"] = value["channel_name"]
    out["OriginEndpointName"] = value["origin_endpoint_name"]
    import aws_sdk_mediapackagev2.types.container_type

    out["ContainerType"] = aws_sdk_mediapackagev2.types.container_type.serialize_json(
        value["container_type"]
    )
    import aws_sdk_mediapackagev2.types.segment

    out["Segment"] = aws_sdk_mediapackagev2.types.segment.serialize_json(
        value["segment"]
    )
    import aws_sdk_mediapackagev2.types._prelude.timestamp

    out["CreatedAt"] = aws_sdk_mediapackagev2.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_mediapackagev2.types._prelude.timestamp

    out["ModifiedAt"] = aws_sdk_mediapackagev2.types._prelude.timestamp.serialize_json(
        value["modified_at"]
    )
    if "description" in value:
        out["Description"] = value["description"]
    if "startover_window_seconds" in value:
        out["StartoverWindowSeconds"] = value["startover_window_seconds"]
    if "hls_manifests" in value:
        import aws_sdk_mediapackagev2.types.get_hls_manifests

        out["HlsManifests"] = (
            aws_sdk_mediapackagev2.types.get_hls_manifests.serialize_json(
                value["hls_manifests"]
            )
        )
    if "low_latency_hls_manifests" in value:
        import aws_sdk_mediapackagev2.types.get_low_latency_hls_manifests

        out["LowLatencyHlsManifests"] = (
            aws_sdk_mediapackagev2.types.get_low_latency_hls_manifests.serialize_json(
                value["low_latency_hls_manifests"]
            )
        )
    if "dash_manifests" in value:
        import aws_sdk_mediapackagev2.types.get_dash_manifests

        out["DashManifests"] = (
            aws_sdk_mediapackagev2.types.get_dash_manifests.serialize_json(
                value["dash_manifests"]
            )
        )
    if "mss_manifests" in value:
        import aws_sdk_mediapackagev2.types.get_mss_manifests

        out["MssManifests"] = (
            aws_sdk_mediapackagev2.types.get_mss_manifests.serialize_json(
                value["mss_manifests"]
            )
        )
    if "force_endpoint_error_configuration" in value:
        import aws_sdk_mediapackagev2.types.force_endpoint_error_configuration

        out["ForceEndpointErrorConfiguration"] = (
            aws_sdk_mediapackagev2.types.force_endpoint_error_configuration.serialize_json(
                value["force_endpoint_error_configuration"]
            )
        )
    if "uri_separator" in value:
        import aws_sdk_mediapackagev2.types.uri_separator

        out["UriSeparator"] = aws_sdk_mediapackagev2.types.uri_separator.serialize_json(
            value["uri_separator"]
        )
    if "e_tag" in value:
        out["ETag"] = value["e_tag"]
    if "tags" in value:
        import aws_sdk_mediapackagev2.types.tag_map

        out["Tags"] = aws_sdk_mediapackagev2.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateOriginEndpointResponse:
    out: CreateOriginEndpointResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("CreateOriginEndpointResponse.arn required")
    if "ChannelGroupName" in data:
        out["channel_group_name"] = data["ChannelGroupName"]
    else:
        raise DeserializationError(
            "CreateOriginEndpointResponse.channel_group_name required"
        )
    if "ChannelName" in data:
        out["channel_name"] = data["ChannelName"]
    else:
        raise DeserializationError("CreateOriginEndpointResponse.channel_name required")
    if "OriginEndpointName" in data:
        out["origin_endpoint_name"] = data["OriginEndpointName"]
    else:
        raise DeserializationError(
            "CreateOriginEndpointResponse.origin_endpoint_name required"
        )
    if "ContainerType" in data:
        import aws_sdk_mediapackagev2.types.container_type

        out["container_type"] = (
            aws_sdk_mediapackagev2.types.container_type.deserialize_json(
                data["ContainerType"]
            )
        )
    else:
        raise DeserializationError(
            "CreateOriginEndpointResponse.container_type required"
        )
    if "Segment" in data:
        import aws_sdk_mediapackagev2.types.segment

        out["segment"] = aws_sdk_mediapackagev2.types.segment.deserialize_json(
            data["Segment"]
        )
    else:
        raise DeserializationError("CreateOriginEndpointResponse.segment required")
    if "CreatedAt" in data:
        import aws_sdk_mediapackagev2.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_mediapackagev2.types._prelude.timestamp.deserialize_json(
                data["CreatedAt"]
            )
        )
    else:
        raise DeserializationError("CreateOriginEndpointResponse.created_at required")
    if "ModifiedAt" in data:
        import aws_sdk_mediapackagev2.types._prelude.timestamp

        out["modified_at"] = (
            aws_sdk_mediapackagev2.types._prelude.timestamp.deserialize_json(
                data["ModifiedAt"]
            )
        )
    else:
        raise DeserializationError("CreateOriginEndpointResponse.modified_at required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "StartoverWindowSeconds" in data:
        out["startover_window_seconds"] = data["StartoverWindowSeconds"]
    if "HlsManifests" in data:
        import aws_sdk_mediapackagev2.types.get_hls_manifests

        out["hls_manifests"] = (
            aws_sdk_mediapackagev2.types.get_hls_manifests.deserialize_json(
                data["HlsManifests"]
            )
        )
    if "LowLatencyHlsManifests" in data:
        import aws_sdk_mediapackagev2.types.get_low_latency_hls_manifests

        out["low_latency_hls_manifests"] = (
            aws_sdk_mediapackagev2.types.get_low_latency_hls_manifests.deserialize_json(
                data["LowLatencyHlsManifests"]
            )
        )
    if "DashManifests" in data:
        import aws_sdk_mediapackagev2.types.get_dash_manifests

        out["dash_manifests"] = (
            aws_sdk_mediapackagev2.types.get_dash_manifests.deserialize_json(
                data["DashManifests"]
            )
        )
    if "MssManifests" in data:
        import aws_sdk_mediapackagev2.types.get_mss_manifests

        out["mss_manifests"] = (
            aws_sdk_mediapackagev2.types.get_mss_manifests.deserialize_json(
                data["MssManifests"]
            )
        )
    if "ForceEndpointErrorConfiguration" in data:
        import aws_sdk_mediapackagev2.types.force_endpoint_error_configuration

        out["force_endpoint_error_configuration"] = (
            aws_sdk_mediapackagev2.types.force_endpoint_error_configuration.deserialize_json(
                data["ForceEndpointErrorConfiguration"]
            )
        )
    if "UriSeparator" in data:
        import aws_sdk_mediapackagev2.types.uri_separator

        out["uri_separator"] = (
            aws_sdk_mediapackagev2.types.uri_separator.deserialize_json(
                data["UriSeparator"]
            )
        )
    if "ETag" in data:
        out["e_tag"] = data["ETag"]
    if "Tags" in data:
        import aws_sdk_mediapackagev2.types.tag_map

        out["tags"] = aws_sdk_mediapackagev2.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out
