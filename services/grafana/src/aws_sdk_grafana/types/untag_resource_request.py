"""Generated from Smithy shape ``com.amazonaws.grafana#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_grafana.types.tag_keys


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "str"
    """<p>The ARN of the resource the tag association is removed from. </p>"""
    tag_keys: "aws_sdk_grafana.types.tag_keys.TagKeys"
    """<p>The key values of the tag to be removed from the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
