"""Generated from Smithy shape ``com.amazonaws.s3files#ListMountTargetsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3files.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3files.types.mount_targets


class ListMountTargetsResponse(TypedDict):
    next_token: NotRequired["str"]
    """<p>A pagination token to use in a subsequent request if more results are available.</p>"""
    mount_targets: "aws_sdk_s3files.types.mount_targets.MountTargets"
    """<p>An array of mount target descriptions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMountTargetsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_s3files.types.mount_targets

    out["mountTargets"] = aws_sdk_s3files.types.mount_targets.serialize_json(
        value["mount_targets"]
    )
    return out


def deserialize_json(data: dict) -> ListMountTargetsResponse:
    out: ListMountTargetsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "mountTargets" in data:
        import aws_sdk_s3files.types.mount_targets

        out["mount_targets"] = aws_sdk_s3files.types.mount_targets.deserialize_json(
            data["mountTargets"]
        )
    else:
        raise DeserializationError("ListMountTargetsResponse.mount_targets required")
    return out
