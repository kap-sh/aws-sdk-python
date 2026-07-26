"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.resource_arn
    import capo_migrationhuborchestrator.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_migrationhuborchestrator.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource from which you want to remove tags.</p>"""
    tag_keys: "capo_migrationhuborchestrator.types.tag_key_list.TagKeyList"
    """<p>One or more tag keys. Specify only the tag keys, not the tag values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
