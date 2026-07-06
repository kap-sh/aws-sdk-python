"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#UpdatePackagingGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediapackage_vod.types.__string
    import aws_sdk_mediapackage_vod.types.authorization


class UpdatePackagingGroupRequest(TypedDict, closed=True):
    authorization: NotRequired[
        "aws_sdk_mediapackage_vod.types.authorization.Authorization"
    ]
    id: "aws_sdk_mediapackage_vod.types.__string.__string"
    """The ID of a MediaPackage VOD PackagingGroup resource."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePackagingGroupRequest) -> dict:
    out: dict = {}
    if "authorization" in value:
        import aws_sdk_mediapackage_vod.types.authorization

        out["authorization"] = (
            aws_sdk_mediapackage_vod.types.authorization.serialize_json(
                value["authorization"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatePackagingGroupRequest:
    out: UpdatePackagingGroupRequest = {}  # type: ignore[typeddict-item]
    if "authorization" in data:
        import aws_sdk_mediapackage_vod.types.authorization

        out["authorization"] = (
            aws_sdk_mediapackage_vod.types.authorization.deserialize_json(
                data["authorization"]
            )
        )
    return out
