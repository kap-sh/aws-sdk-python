"""Generated from Smithy shape ``com.amazonaws.osis#PipelineStatusReason``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_osis.types.string


class PipelineStatusReason(TypedDict, closed=True):
    description: NotRequired["aws_sdk_osis.types.string.String"]
    """<p>A description of why a pipeline has a certain status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PipelineStatusReason) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> PipelineStatusReason:
    out: PipelineStatusReason = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    return out
