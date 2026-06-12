"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#PackagingGroup``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediapackage_vod.types.__integer
    import aws_sdk_mediapackage_vod.types.__string
    import aws_sdk_mediapackage_vod.types.authorization
    import aws_sdk_mediapackage_vod.types.egress_access_logs
    import aws_sdk_mediapackage_vod.types.tags


class PackagingGroup(TypedDict):
    approximate_asset_count: NotRequired[
        "aws_sdk_mediapackage_vod.types.__integer.__integer"
    ]
    """The approximate asset count of the PackagingGroup."""
    arn: NotRequired["aws_sdk_mediapackage_vod.types.__string.__string"]
    """The ARN of the PackagingGroup."""
    authorization: NotRequired[
        "aws_sdk_mediapackage_vod.types.authorization.Authorization"
    ]
    created_at: NotRequired["aws_sdk_mediapackage_vod.types.__string.__string"]
    """The time the PackagingGroup was created."""
    domain_name: NotRequired["aws_sdk_mediapackage_vod.types.__string.__string"]
    """The fully qualified domain name for Assets in the PackagingGroup."""
    egress_access_logs: NotRequired[
        "aws_sdk_mediapackage_vod.types.egress_access_logs.EgressAccessLogs"
    ]
    id: NotRequired["aws_sdk_mediapackage_vod.types.__string.__string"]
    """The ID of the PackagingGroup."""
    tags: NotRequired["aws_sdk_mediapackage_vod.types.tags.Tags"]


# --- restJson1 ser/de ---
def serialize_json(value: PackagingGroup) -> dict:
    out: dict = {}
    if "approximate_asset_count" in value:
        out["approximateAssetCount"] = value["approximate_asset_count"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "authorization" in value:
        import aws_sdk_mediapackage_vod.types.authorization

        out["authorization"] = (
            aws_sdk_mediapackage_vod.types.authorization.serialize_json(
                value["authorization"]
            )
        )
    if "created_at" in value:
        out["createdAt"] = value["created_at"]
    if "domain_name" in value:
        out["domainName"] = value["domain_name"]
    if "egress_access_logs" in value:
        import aws_sdk_mediapackage_vod.types.egress_access_logs

        out["egressAccessLogs"] = (
            aws_sdk_mediapackage_vod.types.egress_access_logs.serialize_json(
                value["egress_access_logs"]
            )
        )
    if "id" in value:
        out["id"] = value["id"]
    if "tags" in value:
        import aws_sdk_mediapackage_vod.types.tags

        out["tags"] = aws_sdk_mediapackage_vod.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> PackagingGroup:
    out: PackagingGroup = {}  # type: ignore[typeddict-item]
    if "approximateAssetCount" in data:
        out["approximate_asset_count"] = data["approximateAssetCount"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "authorization" in data:
        import aws_sdk_mediapackage_vod.types.authorization

        out["authorization"] = (
            aws_sdk_mediapackage_vod.types.authorization.deserialize_json(
                data["authorization"]
            )
        )
    if "createdAt" in data:
        out["created_at"] = data["createdAt"]
    if "domainName" in data:
        out["domain_name"] = data["domainName"]
    if "egressAccessLogs" in data:
        import aws_sdk_mediapackage_vod.types.egress_access_logs

        out["egress_access_logs"] = (
            aws_sdk_mediapackage_vod.types.egress_access_logs.deserialize_json(
                data["egressAccessLogs"]
            )
        )
    if "id" in data:
        out["id"] = data["id"]
    if "tags" in data:
        import aws_sdk_mediapackage_vod.types.tags

        out["tags"] = aws_sdk_mediapackage_vod.types.tags.deserialize_json(data["tags"])
    return out
