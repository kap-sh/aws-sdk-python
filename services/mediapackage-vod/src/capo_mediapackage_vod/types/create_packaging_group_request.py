"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#CreatePackagingGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediapackage_vod.types.__string
    import capo_mediapackage_vod.types.authorization
    import capo_mediapackage_vod.types.egress_access_logs
    import capo_mediapackage_vod.types.tags


class CreatePackagingGroupRequest(TypedDict, closed=True):
    authorization: NotRequired[
        "capo_mediapackage_vod.types.authorization.Authorization"
    ]
    egress_access_logs: NotRequired[
        "capo_mediapackage_vod.types.egress_access_logs.EgressAccessLogs"
    ]
    id: NotRequired["capo_mediapackage_vod.types.__string.__string"]
    """The ID of the PackagingGroup."""
    tags: NotRequired["capo_mediapackage_vod.types.tags.Tags"]


# --- restJson1 ser/de ---
def serialize_json(value: CreatePackagingGroupRequest) -> dict:
    out: dict = {}
    if "authorization" in value:
        import capo_mediapackage_vod.types.authorization

        out["authorization"] = capo_mediapackage_vod.types.authorization.serialize_json(
            value["authorization"]
        )
    if "egress_access_logs" in value:
        import capo_mediapackage_vod.types.egress_access_logs

        out["egressAccessLogs"] = (
            capo_mediapackage_vod.types.egress_access_logs.serialize_json(
                value["egress_access_logs"]
            )
        )
    if "id" in value:
        out["id"] = value["id"]
    if "tags" in value:
        import capo_mediapackage_vod.types.tags

        out["tags"] = capo_mediapackage_vod.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreatePackagingGroupRequest:
    out: CreatePackagingGroupRequest = {}  # type: ignore[typeddict-item]
    if "authorization" in data:
        import capo_mediapackage_vod.types.authorization

        out["authorization"] = (
            capo_mediapackage_vod.types.authorization.deserialize_json(
                data["authorization"]
            )
        )
    if "egressAccessLogs" in data:
        import capo_mediapackage_vod.types.egress_access_logs

        out["egress_access_logs"] = (
            capo_mediapackage_vod.types.egress_access_logs.deserialize_json(
                data["egressAccessLogs"]
            )
        )
    if "id" in data:
        out["id"] = data["id"]
    if "tags" in data:
        import capo_mediapackage_vod.types.tags

        out["tags"] = capo_mediapackage_vod.types.tags.deserialize_json(data["tags"])
    return out
