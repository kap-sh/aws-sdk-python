"""Generated from Smithy shape ``com.amazonaws.signer#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_signer.types.string


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_signer.types.string.String"
    """<p>The Amazon Resource Name (ARN) for the signing profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
