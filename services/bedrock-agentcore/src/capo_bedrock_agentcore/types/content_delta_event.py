"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ContentDeltaEvent``."""

from typing_extensions import NotRequired, TypedDict


class ContentDeltaEvent(TypedDict, closed=True):
    stdout: NotRequired["str"]
    """<p>The standard output content from the command execution. This field contains the incremental output written to stdout by the executing command.</p>"""
    stderr: NotRequired["str"]
    """<p>The standard error content from the command execution. This field contains the incremental output written to stderr by the executing command.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContentDeltaEvent) -> dict:
    out: dict = {}
    if "stdout" in value:
        out["stdout"] = value["stdout"]
    if "stderr" in value:
        out["stderr"] = value["stderr"]
    return out


def deserialize_json(data: dict) -> ContentDeltaEvent:
    out: ContentDeltaEvent = {}  # type: ignore[typeddict-item]
    if data.get("stdout") is not None:
        out["stdout"] = data["stdout"]
    if data.get("stderr") is not None:
        out["stderr"] = data["stderr"]
    return out
