"""Generated from Smithy shape ``com.amazonaws.tnb#FunctionArtifactMeta``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_tnb.types.override_list

class FunctionArtifactMeta(TypedDict):
    overrides: NotRequired["aws_sdk_tnb.types.override_list.OverrideList"]
    """<p>Lists of function package overrides.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: FunctionArtifactMeta) -> dict:
    out: dict = {}
    if "overrides" in value:
        import aws_sdk_tnb.types.override_list
        out["overrides"] = aws_sdk_tnb.types.override_list.serialize_json(value["overrides"])
    return out


def deserialize_json(data: dict) -> FunctionArtifactMeta:
    out: FunctionArtifactMeta = {}  # type: ignore[typeddict-item]
    if "overrides" in data:
        import aws_sdk_tnb.types.override_list
        out["overrides"] = aws_sdk_tnb.types.override_list.deserialize_json(data["overrides"])
    return out