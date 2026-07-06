"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#ListTagsForResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkflowmonitor.types.arn


class ListTagsForResourceInput(TypedDict, closed=True):
    resource_arn: "aws_sdk_networkflowmonitor.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceInput:
    out: ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
    return out
