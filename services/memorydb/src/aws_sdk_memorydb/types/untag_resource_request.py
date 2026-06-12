"""Generated from Smithy shape ``com.amazonaws.memorydb#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_memorydb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.key_list
    import aws_sdk_memorydb.types.string


class UntagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_memorydb.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the resource to which the tags are to be removed.</p>"""
    tag_keys: "aws_sdk_memorydb.types.key_list.KeyList"
    """<p>The list of keys of the tags that are to be removed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import aws_sdk_memorydb.types.key_list

    out["TagKeys"] = aws_sdk_memorydb.types.key_list.serialize_aws_json_1_1(
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
        import aws_sdk_memorydb.types.key_list

        out["tag_keys"] = aws_sdk_memorydb.types.key_list.deserialize_aws_json_1_1(
            data["TagKeys"]
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out
