"""Generated from Smithy shape ``com.amazonaws.guardduty#ActorProcess``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.process_name
    import aws_sdk_guardduty.types.process_path
    import aws_sdk_guardduty.types.process_sha256


class ActorProcess(TypedDict):
    name: NotRequired["aws_sdk_guardduty.types.process_name.ProcessName"]
    """<p>The name of the process as it appears in the system.</p>"""
    path: NotRequired["aws_sdk_guardduty.types.process_path.ProcessPath"]
    """<p>The full file path to the process executable on the system.</p>"""
    sha256: NotRequired["aws_sdk_guardduty.types.process_sha256.ProcessSha256"]
    """<p>The SHA256 hash of the process executable file, which can be used for identification and verification purposes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActorProcess) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "path" in value:
        out["path"] = value["path"]
    if "sha256" in value:
        out["sha256"] = value["sha256"]
    return out


def deserialize_json(data: dict) -> ActorProcess:
    out: ActorProcess = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "path" in data:
        out["path"] = data["path"]
    if "sha256" in data:
        out["sha256"] = data["sha256"]
    return out
