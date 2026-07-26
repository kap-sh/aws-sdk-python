"""Generated from Smithy shape ``com.amazonaws.sagemaker#AddTagsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.tag_list


class AddTagsOutput(TypedDict, closed=True):
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>A list of tags associated with the SageMaker resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddTagsOutput) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AddTagsOutput:
    out: AddTagsOutput = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
