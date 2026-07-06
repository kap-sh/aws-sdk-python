"""Generated from Smithy shape ``com.amazonaws.datasync#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_datasync.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datasync.types.tag_key_list
    import aws_sdk_datasync.types.taggable_resource_arn


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_datasync.types.taggable_resource_arn.TaggableResourceArn"
    """<p>Specifies the Amazon Resource Name (ARN) of the resource to remove the tags from.</p>"""
    keys: "aws_sdk_datasync.types.tag_key_list.TagKeyList"
    """<p>Specifies the keys in the tags that you want to remove.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import aws_sdk_datasync.types.tag_key_list

    out["Keys"] = aws_sdk_datasync.types.tag_key_list.serialize_aws_json_1_1(
        value["keys"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("UntagResourceRequest.resource_arn required")
    if "Keys" in data:
        import aws_sdk_datasync.types.tag_key_list

        out["keys"] = aws_sdk_datasync.types.tag_key_list.deserialize_aws_json_1_1(
            data["Keys"]
        )
    else:
        raise DeserializationError("UntagResourceRequest.keys required")
    return out
