"""Generated from Smithy shape ``com.amazonaws.efs#DescribeMountTargetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_efs.types.marker
    import aws_sdk_efs.types.mount_target_descriptions


class DescribeMountTargetsResponse(TypedDict, closed=True):
    marker: NotRequired["aws_sdk_efs.types.marker.Marker"]
    """<p>If the request included the <code>Marker</code>, the response returns that value in this field.</p>"""
    mount_targets: NotRequired[
        "aws_sdk_efs.types.mount_target_descriptions.MountTargetDescriptions"
    ]
    """<p>Returns the file system's mount targets as an array of <code>MountTargetDescription</code> objects.</p>"""
    next_marker: NotRequired["aws_sdk_efs.types.marker.Marker"]
    """<p>If a value is present, there are more mount targets to return. In a subsequent request, you can provide <code>Marker</code> in your request with this value to retrieve the next set of mount targets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeMountTargetsResponse) -> dict:
    out: dict = {}
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "mount_targets" in value:
        import aws_sdk_efs.types.mount_target_descriptions

        out["MountTargets"] = (
            aws_sdk_efs.types.mount_target_descriptions.serialize_json(
                value["mount_targets"]
            )
        )
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    return out


def deserialize_json(data: dict) -> DescribeMountTargetsResponse:
    out: DescribeMountTargetsResponse = {}  # type: ignore[typeddict-item]
    if "Marker" in data:
        out["marker"] = data["Marker"]
    if "MountTargets" in data:
        import aws_sdk_efs.types.mount_target_descriptions

        out["mount_targets"] = (
            aws_sdk_efs.types.mount_target_descriptions.deserialize_json(
                data["MountTargets"]
            )
        )
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    return out
