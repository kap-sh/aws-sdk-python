"""Generated from Smithy shape ``com.amazonaws.signer#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_signer.types.string
    import aws_sdk_signer.types.tag_key_list


class UntagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_signer.types.string.String"
    """<p>The Amazon Resource Name (ARN) for the signing profile.</p>"""
    tag_keys: "aws_sdk_signer.types.tag_key_list.TagKeyList"
    """<p>A list of tag keys to be removed from the signing profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
