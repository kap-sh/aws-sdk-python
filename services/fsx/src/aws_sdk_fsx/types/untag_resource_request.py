"""Generated from Smithy shape ``com.amazonaws.fsx#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.resource_arn
    import aws_sdk_fsx.types.tag_keys


class UntagResourceRequest(TypedDict):
    resource_arn: NotRequired["aws_sdk_fsx.types.resource_arn.ResourceARN"]
    """<p>The ARN of the Amazon FSx resource to untag.</p>"""
    tag_keys: NotRequired["aws_sdk_fsx.types.tag_keys.TagKeys"]
    """<p>A list of keys of tags on the resource to untag. In case the tag key doesn't exist, the call will still succeed to be idempotent.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceARN"] = value["resource_arn"]
    if "tag_keys" in value:
        import aws_sdk_fsx.types.tag_keys

        out["TagKeys"] = aws_sdk_fsx.types.tag_keys.serialize_aws_json_1_1(
            value["tag_keys"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    if "TagKeys" in data:
        import aws_sdk_fsx.types.tag_keys

        out["tag_keys"] = aws_sdk_fsx.types.tag_keys.deserialize_aws_json_1_1(
            data["TagKeys"]
        )
    return out
