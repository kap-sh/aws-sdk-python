"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteTagsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.resource_arn
    import aws_sdk_sagemaker.types.tag_key_list


class DeleteTagsInput(TypedDict):
    resource_arn: NotRequired["aws_sdk_sagemaker.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the resource whose tags you want to delete.</p>"""
    tag_keys: NotRequired["aws_sdk_sagemaker.types.tag_key_list.TagKeyList"]
    """<p>An array or one or more tag keys to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteTagsInput) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "tag_keys" in value:
        import aws_sdk_sagemaker.types.tag_key_list

        out["TagKeys"] = aws_sdk_sagemaker.types.tag_key_list.serialize_aws_json_1_1(
            value["tag_keys"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteTagsInput:
    out: DeleteTagsInput = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "TagKeys" in data:
        import aws_sdk_sagemaker.types.tag_key_list

        out["tag_keys"] = aws_sdk_sagemaker.types.tag_key_list.deserialize_aws_json_1_1(
            data["TagKeys"]
        )
    return out
