"""Generated from Smithy shape ``com.amazonaws.workspacesweb#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
