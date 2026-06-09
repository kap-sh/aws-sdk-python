"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonVolume``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.host_volume_properties
    import aws_sdk_ecs.types.string


class DaemonVolume(TypedDict):
    name: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The name of the volume. Up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens are allowed.</p>"""
    host: NotRequired["aws_sdk_ecs.types.host_volume_properties.HostVolumeProperties"]
    """<p>The contents of the <code>host</code> parameter determine whether your bind mount host volume persists on the host container instance and where it's stored.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaemonVolume) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "host" in value:
        import aws_sdk_ecs.types.host_volume_properties

        out["host"] = aws_sdk_ecs.types.host_volume_properties.serialize_aws_json_1_1(
            value["host"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DaemonVolume:
    out: DaemonVolume = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "host" in data:
        import aws_sdk_ecs.types.host_volume_properties

        out["host"] = aws_sdk_ecs.types.host_volume_properties.deserialize_aws_json_1_1(
            data["host"]
        )
    return out
