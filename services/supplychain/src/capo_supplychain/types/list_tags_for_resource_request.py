"""Generated from Smithy shape ``com.amazonaws.supplychain#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_supplychain.types.asc_resource_arn


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_supplychain.types.asc_resource_arn.AscResourceArn"
    """<p>The Amazon Web Services Supply chain resource ARN that needs tags to be listed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
