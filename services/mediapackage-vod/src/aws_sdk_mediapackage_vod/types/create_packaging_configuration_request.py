"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#CreatePackagingConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediapackage_vod.types.__string
    import aws_sdk_mediapackage_vod.types.cmaf_package
    import aws_sdk_mediapackage_vod.types.dash_package
    import aws_sdk_mediapackage_vod.types.hls_package
    import aws_sdk_mediapackage_vod.types.mss_package
    import aws_sdk_mediapackage_vod.types.tags


class CreatePackagingConfigurationRequest(TypedDict, closed=True):
    cmaf_package: NotRequired["aws_sdk_mediapackage_vod.types.cmaf_package.CmafPackage"]
    dash_package: NotRequired["aws_sdk_mediapackage_vod.types.dash_package.DashPackage"]
    hls_package: NotRequired["aws_sdk_mediapackage_vod.types.hls_package.HlsPackage"]
    id: NotRequired["aws_sdk_mediapackage_vod.types.__string.__string"]
    """The ID of the PackagingConfiguration."""
    mss_package: NotRequired["aws_sdk_mediapackage_vod.types.mss_package.MssPackage"]
    packaging_group_id: NotRequired["aws_sdk_mediapackage_vod.types.__string.__string"]
    """The ID of a PackagingGroup."""
    tags: NotRequired["aws_sdk_mediapackage_vod.types.tags.Tags"]


# --- restJson1 ser/de ---
def serialize_json(value: CreatePackagingConfigurationRequest) -> dict:
    out: dict = {}
    if "cmaf_package" in value:
        import aws_sdk_mediapackage_vod.types.cmaf_package

        out["cmafPackage"] = aws_sdk_mediapackage_vod.types.cmaf_package.serialize_json(
            value["cmaf_package"]
        )
    if "dash_package" in value:
        import aws_sdk_mediapackage_vod.types.dash_package

        out["dashPackage"] = aws_sdk_mediapackage_vod.types.dash_package.serialize_json(
            value["dash_package"]
        )
    if "hls_package" in value:
        import aws_sdk_mediapackage_vod.types.hls_package

        out["hlsPackage"] = aws_sdk_mediapackage_vod.types.hls_package.serialize_json(
            value["hls_package"]
        )
    if "id" in value:
        out["id"] = value["id"]
    if "mss_package" in value:
        import aws_sdk_mediapackage_vod.types.mss_package

        out["mssPackage"] = aws_sdk_mediapackage_vod.types.mss_package.serialize_json(
            value["mss_package"]
        )
    if "packaging_group_id" in value:
        out["packagingGroupId"] = value["packaging_group_id"]
    if "tags" in value:
        import aws_sdk_mediapackage_vod.types.tags

        out["tags"] = aws_sdk_mediapackage_vod.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreatePackagingConfigurationRequest:
    out: CreatePackagingConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "cmafPackage" in data:
        import aws_sdk_mediapackage_vod.types.cmaf_package

        out["cmaf_package"] = (
            aws_sdk_mediapackage_vod.types.cmaf_package.deserialize_json(
                data["cmafPackage"]
            )
        )
    if "dashPackage" in data:
        import aws_sdk_mediapackage_vod.types.dash_package

        out["dash_package"] = (
            aws_sdk_mediapackage_vod.types.dash_package.deserialize_json(
                data["dashPackage"]
            )
        )
    if "hlsPackage" in data:
        import aws_sdk_mediapackage_vod.types.hls_package

        out["hls_package"] = (
            aws_sdk_mediapackage_vod.types.hls_package.deserialize_json(
                data["hlsPackage"]
            )
        )
    if "id" in data:
        out["id"] = data["id"]
    if "mssPackage" in data:
        import aws_sdk_mediapackage_vod.types.mss_package

        out["mss_package"] = (
            aws_sdk_mediapackage_vod.types.mss_package.deserialize_json(
                data["mssPackage"]
            )
        )
    if "packagingGroupId" in data:
        out["packaging_group_id"] = data["packagingGroupId"]
    if "tags" in data:
        import aws_sdk_mediapackage_vod.types.tags

        out["tags"] = aws_sdk_mediapackage_vod.types.tags.deserialize_json(data["tags"])
    return out
