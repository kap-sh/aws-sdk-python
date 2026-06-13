"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#UpdateOriginEndpointRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mediapackagev2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediapackagev2.types.container_type
    import aws_sdk_mediapackagev2.types.create_dash_manifests
    import aws_sdk_mediapackagev2.types.create_hls_manifests
    import aws_sdk_mediapackagev2.types.create_low_latency_hls_manifests
    import aws_sdk_mediapackagev2.types.create_mss_manifests
    import aws_sdk_mediapackagev2.types.entity_tag
    import aws_sdk_mediapackagev2.types.force_endpoint_error_configuration
    import aws_sdk_mediapackagev2.types.resource_description
    import aws_sdk_mediapackagev2.types.resource_name
    import aws_sdk_mediapackagev2.types.segment
    import aws_sdk_mediapackagev2.types.uri_separator


class UpdateOriginEndpointRequest(TypedDict):
    channel_group_name: "aws_sdk_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.</p>"""
    channel_name: "aws_sdk_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. </p>"""
    origin_endpoint_name: "aws_sdk_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name that describes the origin endpoint. The name is the primary identifier for the origin endpoint, and and must be unique for your account in the AWS Region and channel. </p>"""
    container_type: "aws_sdk_mediapackagev2.types.container_type.ContainerType"
    """<p>The type of container attached to this origin endpoint. A container type is a file format that encapsulates one or more media streams, such as audio and video, into a single file. </p>"""
    segment: NotRequired["aws_sdk_mediapackagev2.types.segment.Segment"]
    """<p>The segment configuration, including the segment name, duration, and other configuration values.</p>"""
    description: NotRequired[
        "aws_sdk_mediapackagev2.types.resource_description.ResourceDescription"
    ]
    """<p>Any descriptive information that you want to add to the origin endpoint for future identification purposes.</p>"""
    startover_window_seconds: NotRequired["int"]
    """<p>The size of the window (in seconds) to create a window of the live stream that's available for on-demand viewing. Viewers can start-over or catch-up on content that falls within the window. The maximum startover window is 1,209,600 seconds (14 days).</p>"""
    hls_manifests: NotRequired[
        "aws_sdk_mediapackagev2.types.create_hls_manifests.CreateHlsManifests"
    ]
    """<p>An HTTP live streaming (HLS) manifest configuration.</p>"""
    low_latency_hls_manifests: NotRequired[
        "aws_sdk_mediapackagev2.types.create_low_latency_hls_manifests.CreateLowLatencyHlsManifests"
    ]
    """<p>A low-latency HLS manifest configuration.</p>"""
    dash_manifests: NotRequired[
        "aws_sdk_mediapackagev2.types.create_dash_manifests.CreateDashManifests"
    ]
    """<p>A DASH manifest configuration.</p>"""
    mss_manifests: NotRequired[
        "aws_sdk_mediapackagev2.types.create_mss_manifests.CreateMssManifests"
    ]
    """<p>A list of Microsoft Smooth Streaming (MSS) manifest configurations to update for the origin endpoint. This replaces the existing MSS manifest configurations.</p>"""
    force_endpoint_error_configuration: NotRequired[
        "aws_sdk_mediapackagev2.types.force_endpoint_error_configuration.ForceEndpointErrorConfiguration"
    ]
    """<p>The failover settings for the endpoint.</p>"""
    uri_separator: NotRequired[
        "aws_sdk_mediapackagev2.types.uri_separator.UriSeparator"
    ]
    """<p>The separator character to use in generated URIs for this origin endpoint. This setting applies to all manifest types on the endpoint. If you don't specify a value in the update request, the current value is preserved.</p>"""
    e_tag: NotRequired["aws_sdk_mediapackagev2.types.entity_tag.EntityTag"]
    """<p>The expected current Entity Tag (ETag) for the resource. If the specified ETag does not match the resource's current entity tag, the update request will be rejected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateOriginEndpointRequest) -> dict:
    out: dict = {}
    import aws_sdk_mediapackagev2.types.container_type

    out["ContainerType"] = aws_sdk_mediapackagev2.types.container_type.serialize_json(
        value["container_type"]
    )
    if "segment" in value:
        import aws_sdk_mediapackagev2.types.segment

        out["Segment"] = aws_sdk_mediapackagev2.types.segment.serialize_json(
            value["segment"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "startover_window_seconds" in value:
        out["StartoverWindowSeconds"] = value["startover_window_seconds"]
    if "hls_manifests" in value:
        import aws_sdk_mediapackagev2.types.create_hls_manifests

        out["HlsManifests"] = (
            aws_sdk_mediapackagev2.types.create_hls_manifests.serialize_json(
                value["hls_manifests"]
            )
        )
    if "low_latency_hls_manifests" in value:
        import aws_sdk_mediapackagev2.types.create_low_latency_hls_manifests

        out["LowLatencyHlsManifests"] = (
            aws_sdk_mediapackagev2.types.create_low_latency_hls_manifests.serialize_json(
                value["low_latency_hls_manifests"]
            )
        )
    if "dash_manifests" in value:
        import aws_sdk_mediapackagev2.types.create_dash_manifests

        out["DashManifests"] = (
            aws_sdk_mediapackagev2.types.create_dash_manifests.serialize_json(
                value["dash_manifests"]
            )
        )
    if "mss_manifests" in value:
        import aws_sdk_mediapackagev2.types.create_mss_manifests

        out["MssManifests"] = (
            aws_sdk_mediapackagev2.types.create_mss_manifests.serialize_json(
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
    return out


def deserialize_json(data: dict) -> UpdateOriginEndpointRequest:
    out: UpdateOriginEndpointRequest = {}  # type: ignore[typeddict-item]
    if "ContainerType" in data:
        import aws_sdk_mediapackagev2.types.container_type

        out["container_type"] = (
            aws_sdk_mediapackagev2.types.container_type.deserialize_json(
                data["ContainerType"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateOriginEndpointRequest.container_type required"
        )
    if "Segment" in data:
        import aws_sdk_mediapackagev2.types.segment

        out["segment"] = aws_sdk_mediapackagev2.types.segment.deserialize_json(
            data["Segment"]
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "StartoverWindowSeconds" in data:
        out["startover_window_seconds"] = data["StartoverWindowSeconds"]
    if "HlsManifests" in data:
        import aws_sdk_mediapackagev2.types.create_hls_manifests

        out["hls_manifests"] = (
            aws_sdk_mediapackagev2.types.create_hls_manifests.deserialize_json(
                data["HlsManifests"]
            )
        )
    if "LowLatencyHlsManifests" in data:
        import aws_sdk_mediapackagev2.types.create_low_latency_hls_manifests

        out["low_latency_hls_manifests"] = (
            aws_sdk_mediapackagev2.types.create_low_latency_hls_manifests.deserialize_json(
                data["LowLatencyHlsManifests"]
            )
        )
    if "DashManifests" in data:
        import aws_sdk_mediapackagev2.types.create_dash_manifests

        out["dash_manifests"] = (
            aws_sdk_mediapackagev2.types.create_dash_manifests.deserialize_json(
                data["DashManifests"]
            )
        )
    if "MssManifests" in data:
        import aws_sdk_mediapackagev2.types.create_mss_manifests

        out["mss_manifests"] = (
            aws_sdk_mediapackagev2.types.create_mss_manifests.deserialize_json(
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
    return out
