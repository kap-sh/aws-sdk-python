"""Generated from Smithy shape ``com.amazonaws.ssmsap#DeleteResourcePermissionOutput``."""

from typing_extensions import NotRequired, TypedDict


class DeleteResourcePermissionOutput(TypedDict, closed=True):
    policy: NotRequired["str"]
    """<p>The policy that removes permissions on the target database.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteResourcePermissionOutput) -> dict:
    out: dict = {}
    if "policy" in value:
        out["Policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> DeleteResourcePermissionOutput:
    out: DeleteResourcePermissionOutput = {}  # type: ignore[typeddict-item]
    if "Policy" in data:
        out["policy"] = data["Policy"]
    return out
