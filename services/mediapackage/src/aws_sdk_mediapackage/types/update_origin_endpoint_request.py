"""Generated from Smithy shape ``com.amazonaws.mediapackage#UpdateOriginEndpointRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediapackage.types.__integer
    import aws_sdk_mediapackage.types.__list_of__string
    import aws_sdk_mediapackage.types.__string
    import aws_sdk_mediapackage.types.authorization
    import aws_sdk_mediapackage.types.cmaf_package_create_or_update_parameters
    import aws_sdk_mediapackage.types.dash_package
    import aws_sdk_mediapackage.types.hls_package
    import aws_sdk_mediapackage.types.mss_package
    import aws_sdk_mediapackage.types.origination


class UpdateOriginEndpointRequest(TypedDict):
    authorization: NotRequired["aws_sdk_mediapackage.types.authorization.Authorization"]
    cmaf_package: NotRequired[
        "aws_sdk_mediapackage.types.cmaf_package_create_or_update_parameters.CmafPackageCreateOrUpdateParameters"
    ]
    dash_package: NotRequired["aws_sdk_mediapackage.types.dash_package.DashPackage"]
    description: NotRequired["aws_sdk_mediapackage.types.__string.__string"]
    """A short text description of the OriginEndpoint."""
    hls_package: NotRequired["aws_sdk_mediapackage.types.hls_package.HlsPackage"]
    id: "aws_sdk_mediapackage.types.__string.__string"
    """The ID of the OriginEndpoint to update."""
    manifest_name: NotRequired["aws_sdk_mediapackage.types.__string.__string"]
    """A short string that will be appended to the end of the Endpoint URL."""
    mss_package: NotRequired["aws_sdk_mediapackage.types.mss_package.MssPackage"]
    origination: NotRequired["aws_sdk_mediapackage.types.origination.Origination"]
    """Control whether origination of video is allowed for this OriginEndpoint. If set to ALLOW, the OriginEndpoint may by requested, pursuant to any other form of access control. If set to DENY, the OriginEndpoint may not be requested. This can be helpful for Live to VOD harvesting, or for temporarily disabling origination"""
    startover_window_seconds: NotRequired[
        "aws_sdk_mediapackage.types.__integer.__integer"
    ]
    """Maximum duration (in seconds) of content to retain for startover playback. If not specified, startover playback will be disabled for the OriginEndpoint."""
    time_delay_seconds: NotRequired["aws_sdk_mediapackage.types.__integer.__integer"]
    """Amount of delay (in seconds) to enforce on the playback of live content. If not specified, there will be no time delay in effect for the OriginEndpoint."""
    whitelist: NotRequired[
        "aws_sdk_mediapackage.types.__list_of__string.__listOf__string"
    ]
    """A list of source IP CIDR blocks that will be allowed to access the OriginEndpoint."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateOriginEndpointRequest) -> dict:
    out: dict = {}
    if "authorization" in value:
        import aws_sdk_mediapackage.types.authorization

        out["authorization"] = aws_sdk_mediapackage.types.authorization.serialize_json(
            value["authorization"]
        )
    if "cmaf_package" in value:
        import aws_sdk_mediapackage.types.cmaf_package_create_or_update_parameters

        out["cmafPackage"] = (
            aws_sdk_mediapackage.types.cmaf_package_create_or_update_parameters.serialize_json(
                value["cmaf_package"]
            )
        )
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
    if "time_delay_seconds" in value:
        out["timeDelaySeconds"] = value["time_delay_seconds"]
    if "whitelist" in value:
        import aws_sdk_mediapackage.types.__list_of__string

        out["whitelist"] = aws_sdk_mediapackage.types.__list_of__string.serialize_json(
            value["whitelist"]
        )
    return out


def deserialize_json(data: dict) -> UpdateOriginEndpointRequest:
    out: UpdateOriginEndpointRequest = {}  # type: ignore[typeddict-item]
    if "authorization" in data:
        import aws_sdk_mediapackage.types.authorization

        out["authorization"] = (
            aws_sdk_mediapackage.types.authorization.deserialize_json(
                data["authorization"]
            )
        )
    if "cmafPackage" in data:
        import aws_sdk_mediapackage.types.cmaf_package_create_or_update_parameters

        out["cmaf_package"] = (
            aws_sdk_mediapackage.types.cmaf_package_create_or_update_parameters.deserialize_json(
                data["cmafPackage"]
            )
        )
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
    if "timeDelaySeconds" in data:
        out["time_delay_seconds"] = data["timeDelaySeconds"]
    if "whitelist" in data:
        import aws_sdk_mediapackage.types.__list_of__string

        out["whitelist"] = (
            aws_sdk_mediapackage.types.__list_of__string.deserialize_json(
                data["whitelist"]
            )
        )
    return out
