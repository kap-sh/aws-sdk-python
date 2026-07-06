"""Generated from Smithy shape ``com.amazonaws.guardduty#Volume``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.host_path
    import aws_sdk_guardduty.types.string


class Volume(TypedDict, closed=True):
    name: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>Volume name.</p>"""
    host_path: NotRequired["aws_sdk_guardduty.types.host_path.HostPath"]
    """<p>Represents a pre-existing file or directory on the host machine that the volume maps to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Volume) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "host_path" in value:
        import aws_sdk_guardduty.types.host_path

        out["hostPath"] = aws_sdk_guardduty.types.host_path.serialize_json(
            value["host_path"]
        )
    return out


def deserialize_json(data: dict) -> Volume:
    out: Volume = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "hostPath" in data:
        import aws_sdk_guardduty.types.host_path

        out["host_path"] = aws_sdk_guardduty.types.host_path.deserialize_json(
            data["hostPath"]
        )
    return out
