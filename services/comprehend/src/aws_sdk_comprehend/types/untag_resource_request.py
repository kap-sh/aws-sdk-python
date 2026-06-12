"""Generated from Smithy shape ``com.amazonaws.comprehend#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.comprehend_arn
    import aws_sdk_comprehend.types.tag_key_list


class UntagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_comprehend.types.comprehend_arn.ComprehendArn"
    """<p> The Amazon Resource Name (ARN) of the given Amazon Comprehend resource from which you want to remove the tags. </p>"""
    tag_keys: "aws_sdk_comprehend.types.tag_key_list.TagKeyList"
    """<p>The initial part of a key-value pair that forms a tag being removed from a given resource. For example, a tag with \"Sales\" as the key might be added to a resource to indicate its use by the sales department. Keys must be unique and cannot be duplicated for a particular resource. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import aws_sdk_comprehend.types.tag_key_list

    out["TagKeys"] = aws_sdk_comprehend.types.tag_key_list.serialize_aws_json_1_1(
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
        import aws_sdk_comprehend.types.tag_key_list

        out["tag_keys"] = (
            aws_sdk_comprehend.types.tag_key_list.deserialize_aws_json_1_1(
                data["TagKeys"]
            )
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out
