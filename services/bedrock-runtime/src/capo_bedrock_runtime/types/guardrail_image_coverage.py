"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailImageCoverage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.images_guarded
    import capo_bedrock_runtime.types.images_total


class GuardrailImageCoverage(TypedDict, closed=True):
    guarded: NotRequired["capo_bedrock_runtime.types.images_guarded.ImagesGuarded"]
    """<p>The count (integer) of images guardrails guarded.</p>"""
    total: NotRequired["capo_bedrock_runtime.types.images_total.ImagesTotal"]
    """<p>Represents the total number of images (integer) that were in the request (guarded and unguarded).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailImageCoverage) -> dict:
    out: dict = {}
    if "guarded" in value:
        out["guarded"] = value["guarded"]
    if "total" in value:
        out["total"] = value["total"]
    return out


def deserialize_json(data: dict) -> GuardrailImageCoverage:
    out: GuardrailImageCoverage = {}  # type: ignore[typeddict-item]
    if "guarded" in data:
        out["guarded"] = data["guarded"]
    if "total" in data:
        out["total"] = data["total"]
    return out
