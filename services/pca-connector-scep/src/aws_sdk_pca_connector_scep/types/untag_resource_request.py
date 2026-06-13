"""Generated from Smithy shape ``com.amazonaws.pcaconnectorscep#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pca_connector_scep.types.tag_key_list


class UntagResourceRequest(TypedDict):
    resource_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    tag_keys: "aws_sdk_pca_connector_scep.types.tag_key_list.TagKeyList"
    """<p>Specifies a list of tag keys that you want to remove from the specified resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
