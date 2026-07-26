"""Generated from Smithy shape ``com.amazonaws.dsql#UntagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_dsql.types.arn
    import capo_dsql.types.tag_key_list


class UntagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_dsql.types.arn.Arn"
    """<p>The ARN of the resource from which to remove tags.</p>"""
    tag_keys: "capo_dsql.types.tag_key_list.TagKeyList"
    """<p>The array of keys of the tags that you want to remove.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    return out
