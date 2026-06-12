"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_global_accelerator.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.resource_arn
    import aws_sdk_global_accelerator.types.tag_keys


class UntagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_global_accelerator.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the Global Accelerator resource to remove tags from. An ARN uniquely identifies a resource.</p>"""
    tag_keys: "aws_sdk_global_accelerator.types.tag_keys.TagKeys"
    """<p>The tag key pairs that you want to remove from the specified resources.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import aws_sdk_global_accelerator.types.tag_keys

    out["TagKeys"] = aws_sdk_global_accelerator.types.tag_keys.serialize_aws_json_1_1(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("UntagResourceRequest.resource_arn required")
    if "TagKeys" in data:
        import aws_sdk_global_accelerator.types.tag_keys

        out["tag_keys"] = (
            aws_sdk_global_accelerator.types.tag_keys.deserialize_aws_json_1_1(
                data["TagKeys"]
            )
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out
