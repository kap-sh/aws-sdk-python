"""Generated from Smithy shape ``com.amazonaws.appsync#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.resource_arn
    import capo_appsync.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_appsync.types.resource_arn.ResourceArn"
    """<p>The <code>GraphqlApi</code> Amazon Resource Name (ARN).</p>"""
    tag_keys: "capo_appsync.types.tag_key_list.TagKeyList"
    """<p>A list of <code>TagKey</code> objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
