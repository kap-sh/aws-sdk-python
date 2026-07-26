"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteTagsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.resource_arn
    import capo_sagemaker.types.tag_key_list


class DeleteTagsInput(TypedDict, closed=True):
    resource_arn: NotRequired["capo_sagemaker.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the resource whose tags you want to delete.</p>"""
    tag_keys: NotRequired["capo_sagemaker.types.tag_key_list.TagKeyList"]
    """<p>An array or one or more tag keys to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteTagsInput) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "tag_keys" in value:
        import capo_sagemaker.types.tag_key_list

        out["TagKeys"] = capo_sagemaker.types.tag_key_list.serialize_aws_json_1_1(
            value["tag_keys"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteTagsInput:
    out: DeleteTagsInput = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "TagKeys" in data:
        import capo_sagemaker.types.tag_key_list

        out["tag_keys"] = capo_sagemaker.types.tag_key_list.deserialize_aws_json_1_1(
            data["TagKeys"]
        )
    return out
