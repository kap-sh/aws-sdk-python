"""Generated from Smithy shape ``com.amazonaws.mediapackage#CreateOriginEndpointResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediapackage.types.__integer
    import aws_sdk_mediapackage.types.__list_of__string
    import aws_sdk_mediapackage.types.__string
    import aws_sdk_mediapackage.types.authorization
    import aws_sdk_mediapackage.types.cmaf_package
    import aws_sdk_mediapackage.types.dash_package
    import aws_sdk_mediapackage.types.hls_package
    import aws_sdk_mediapackage.types.mss_package
    import aws_sdk_mediapackage.types.origination
    import aws_sdk_mediapackage.types.tags


class CreateOriginEndpointResponse(TypedDict):
    arn: NotRequired["aws_sdk_mediapackage.types.__string.__string"]
    """The Amazon Resource Name (ARN) assigned to the OriginEndpoint."""
    authorization: NotRequired["aws_sdk_mediapackage.types.authorization.Authorization"]
    channel_id: NotRequired["aws_sdk_mediapackage.types.__string.__string"]
    """The ID of the Channel the OriginEndpoint is associated with."""
    cmaf_package: NotRequired["aws_sdk_mediapackage.types.cmaf_package.CmafPackage"]
    created_at: NotRequired["aws_sdk_mediapackage.types.__string.__string"]
    """The date and time the OriginEndpoint was created."""
    dash_package: NotRequired["aws_sdk_mediapackage.types.dash_package.DashPackage"]
    description: NotRequired["aws_sdk_mediapackage.types.__string.__string"]
    """A short text description of the OriginEndpoint."""
    hls_package: NotRequired["aws_sdk_mediapackage.types.hls_package.HlsPackage"]
    id: NotRequired["aws_sdk_mediapackage.types.__string.__string"]
    """The ID of the OriginEndpoint."""
    manifest_name: NotRequired["aws_sdk_mediapackage.types.__string.__string"]
    """A short string appended to the end of the OriginEndpoint URL."""
    mss_package: NotRequired["aws_sdk_mediapackage.types.mss_package.MssPackage"]
    origination: NotRequired["aws_sdk_mediapackage.types.origination.Origination"]
    """Control whether origination of video is allowed for this OriginEndpoint. If set to ALLOW, the OriginEndpoint may by requested, pursuant to any other form of access control. If set to DENY, the OriginEndpoint may not be requested. This can be helpful for Live to VOD harvesting, or for temporarily disabling origination"""
    startover_window_seconds: NotRequired[
        "aws_sdk_mediapackage.types.__integer.__integer"
    ]
    """Maximum duration (seconds) of content to retain for startover playback. If not specified, startover playback will be disabled for the OriginEndpoint."""
    tags: NotRequired["aws_sdk_mediapackage.types.tags.Tags"]
    time_delay_seconds: NotRequired["aws_sdk_mediapackage.types.__integer.__integer"]
    """Amount of delay (seconds) to enforce on the playback of live content. If not specified, there will be no time delay in effect for the OriginEndpoint."""
    url: NotRequired["aws_sdk_mediapackage.types.__string.__string"]
    """The URL of the packaged OriginEndpoint for consumption."""
    whitelist: NotRequired[
        "aws_sdk_mediapackage.types.__list_of__string.__listOf__string"
    ]
    """A list of source IP CIDR blocks that will be allowed to access the OriginEndpoint."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateOriginEndpointResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "authorization" in value:
        import aws_sdk_mediapackage.types.authorization

        out["authorization"] = aws_sdk_mediapackage.types.authorization.serialize_json(
            value["authorization"]
        )
    if "channel_id" in value:
        out["channelId"] = value["channel_id"]
    if "cmaf_package" in value:
        import aws_sdk_mediapackage.types.cmaf_package

        out["cmafPackage"] = aws_sdk_mediapackage.types.cmaf_package.serialize_json(
            value["cmaf_package"]
        )
    if "created_at" in value:
        out["createdAt"] = value["created_at"]
    if "dash_package" in value:
        import aws_sdk_mediapackage.types.dash_package

        out["dashPackage"] = aws_sdk_mediapackage.types.dash_package.serialize_json(
            value["dash_package"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "hls_package" in value:
        import aws_sdk_mediapackage.types.hls_package

        out["hlsPackage"] = aws_sdk_mediapackage.types.hls_package.serialize_json(
            value["hls_package"]
        )
    if "id" in value:
        out["id"] = value["id"]
    if "manifest_name" in value:
        out["manifestName"] = value["manifest_name"]
    if "mss_package" in value:
        import aws_sdk_mediapackage.types.mss_package

        out["mssPackage"] = aws_sdk_mediapackage.types.mss_package.serialize_json(
            value["mss_package"]
        )
    if "origination" in value:
        import aws_sdk_mediapackage.types.origination

        out["origination"] = aws_sdk_mediapackage.types.origination.serialize_json(
            value["origination"]
        )
    if "startover_window_seconds" in value:
        out["startoverWindowSeconds"] = value["startover_window_seconds"]
    if "tags" in value:
        import aws_sdk_mediapackage.types.tags

        out["tags"] = aws_sdk_mediapackage.types.tags.serialize_json(value["tags"])
    if "time_delay_seconds" in value:
        out["timeDelaySeconds"] = value["time_delay_seconds"]
    if "url" in value:
        out["url"] = value["url"]
    if "whitelist" in value:
        import aws_sdk_mediapackage.types.__list_of__string

        out["whitelist"] = aws_sdk_mediapackage.types.__list_of__string.serialize_json(
            value["whitelist"]
        )
    return out


def deserialize_json(data: dict) -> CreateOriginEndpointResponse:
    out: CreateOriginEndpointResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "authorization" in data:
        import aws_sdk_mediapackage.types.authorization

        out["authorization"] = (
            aws_sdk_mediapackage.types.authorization.deserialize_json(
                data["authorization"]
            )
        )
    if "channelId" in data:
        out["channel_id"] = data["channelId"]
    if "cmafPackage" in data:
        import aws_sdk_mediapackage.types.cmaf_package

        out["cmaf_package"] = aws_sdk_mediapackage.types.cmaf_package.deserialize_json(
            data["cmafPackage"]
        )
    if "createdAt" in data:
        out["created_at"] = data["createdAt"]
    if "dashPackage" in data:
        import aws_sdk_mediapackage.types.dash_package

        out["dash_package"] = aws_sdk_mediapackage.types.dash_package.deserialize_json(
            data["dashPackage"]
        )
    if "description" in data:
        out["description"] = data["description"]
    if "hlsPackage" in data:
        import aws_sdk_mediapackage.types.hls_package

        out["hls_package"] = aws_sdk_mediapackage.types.hls_package.deserialize_json(
            data["hlsPackage"]
        )
    if "id" in data:
        out["id"] = data["id"]
    if "manifestName" in data:
        out["manifest_name"] = data["manifestName"]
    if "mssPackage" in data:
        import aws_sdk_mediapackage.types.mss_package

        out["mss_package"] = aws_sdk_mediapackage.types.mss_package.deserialize_json(
            data["mssPackage"]
        )
    if "origination" in data:
        import aws_sdk_mediapackage.types.origination

        out["origination"] = aws_sdk_mediapackage.types.origination.deserialize_json(
            data["origination"]
        )
    if "startoverWindowSeconds" in data:
        out["startover_window_seconds"] = data["startoverWindowSeconds"]
    if "tags" in data:
        import aws_sdk_mediapackage.types.tags

        out["tags"] = aws_sdk_mediapackage.types.tags.deserialize_json(data["tags"])
    if "timeDelaySeconds" in data:
        out["time_delay_seconds"] = data["timeDelaySeconds"]
    if "url" in data:
        out["url"] = data["url"]
    if "whitelist" in data:
        import aws_sdk_mediapackage.types.__list_of__string

        out["whitelist"] = (
            aws_sdk_mediapackage.types.__list_of__string.deserialize_json(
                data["whitelist"]
            )
        )
    return out
