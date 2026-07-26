"""Generated from Smithy shape ``com.amazonaws.medicalimaging#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_medical_imaging.types.arn


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_medical_imaging.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the medical imaging resource to list tags for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
