"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.arn
    import aws_sdk_sagemaker_geospatial.types.tag_key_list


class UntagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_sagemaker_geospatial.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the resource you want to untag.</p>"""
    tag_keys: "aws_sdk_sagemaker_geospatial.types.tag_key_list.TagKeyList"
    """<p>Keys of the tags you want to remove.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
