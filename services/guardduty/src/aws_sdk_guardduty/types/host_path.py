"""Generated from Smithy shape ``com.amazonaws.guardduty#HostPath``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.string


class HostPath(TypedDict):
    path: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>Path of the file or directory on the host that the volume maps to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HostPath) -> dict:
    out: dict = {}
    if "path" in value:
        out["path"] = value["path"]
    return out


def deserialize_json(data: dict) -> HostPath:
    out: HostPath = {}  # type: ignore[typeddict-item]
    if "path" in data:
        out["path"] = data["path"]
    return out
