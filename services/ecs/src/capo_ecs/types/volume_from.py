"""Generated from Smithy shape ``com.amazonaws.ecs#VolumeFrom``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.boxed_boolean
    import capo_ecs.types.string


class VolumeFrom(TypedDict, closed=True):
    source_container: NotRequired["capo_ecs.types.string.String"]
    """<p>The name of another container within the same task definition to mount volumes from.</p>"""
    read_only: NotRequired["capo_ecs.types.boxed_boolean.BoxedBoolean"]
    """<p>If this value is <code>true</code>, the container has read-only access to the volume. If this value is <code>false</code>, then the container can write to the volume. The default value is <code>false</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VolumeFrom) -> dict:
    out: dict = {}
    if "source_container" in value:
        out["sourceContainer"] = value["source_container"]
    if "read_only" in value:
        out["readOnly"] = value["read_only"]
    return out


def deserialize_aws_json_1_1(data: dict) -> VolumeFrom:
    out: VolumeFrom = {}  # type: ignore[typeddict-item]
    if "sourceContainer" in data:
        out["source_container"] = data["sourceContainer"]
    if "readOnly" in data:
        out["read_only"] = data["readOnly"]
    return out
