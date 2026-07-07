"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsMountPoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsMountPoint(TypedDict, closed=True):
    source_volume: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the volume to mount. Must be a volume name referenced in the <code>name</code> parameter of task definition <code>volume</code>. </p>"""
    container_path: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The path on the container to mount the host volume at. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsMountPoint) -> dict:
    out: dict = {}
    if "source_volume" in value:
        out["SourceVolume"] = value["source_volume"]
    if "container_path" in value:
        out["ContainerPath"] = value["container_path"]
    return out


def deserialize_json(data: dict) -> AwsMountPoint:
    out: AwsMountPoint = {}  # type: ignore[typeddict-item]
    if "SourceVolume" in data:
        out["source_volume"] = data["SourceVolume"]
    if "ContainerPath" in data:
        out["container_path"] = data["ContainerPath"]
    return out
