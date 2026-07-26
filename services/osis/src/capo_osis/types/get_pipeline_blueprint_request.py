"""Generated from Smithy shape ``com.amazonaws.osis#GetPipelineBlueprintRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_osis.types.blueprint_format
    import capo_osis.types.string


class GetPipelineBlueprintRequest(TypedDict, closed=True):
    blueprint_name: "capo_osis.types.string.String"
    """<p>The name of the blueprint to retrieve.</p>"""
    format: NotRequired["capo_osis.types.blueprint_format.BlueprintFormat"]
    """<p>The format format of the blueprint to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPipelineBlueprintRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPipelineBlueprintRequest:
    out: GetPipelineBlueprintRequest = {}  # type: ignore[typeddict-item]
    return out
