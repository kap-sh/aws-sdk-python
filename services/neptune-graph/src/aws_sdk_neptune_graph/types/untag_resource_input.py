"""Generated from Smithy shape ``com.amazonaws.neptunegraph#UntagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_neptune_graph.types.arn
    import aws_sdk_neptune_graph.types.tag_key_list


class UntagResourceInput(TypedDict, closed=True):
    resource_arn: "aws_sdk_neptune_graph.types.arn.Arn"
    """<p>ARN of the resource whose tag needs to be removed.</p>"""
    tag_keys: "aws_sdk_neptune_graph.types.tag_key_list.TagKeyList"
    """<p>Tag keys for the tags to be removed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    return out
