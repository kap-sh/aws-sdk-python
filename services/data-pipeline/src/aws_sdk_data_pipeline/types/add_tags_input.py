"""Generated from Smithy shape ``com.amazonaws.datapipeline#AddTagsInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_data_pipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_data_pipeline.types.id
    import aws_sdk_data_pipeline.types.tag_list


class AddTagsInput(TypedDict):
    pipeline_id: "aws_sdk_data_pipeline.types.id.id"
    """<p>The ID of the pipeline.</p>"""
    tags: "aws_sdk_data_pipeline.types.tag_list.tagList"
    """<p>The tags to add, as key/value pairs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddTagsInput) -> dict:
    out: dict = {}
    out["pipelineId"] = value["pipeline_id"]
    import aws_sdk_data_pipeline.types.tag_list

    out["tags"] = aws_sdk_data_pipeline.types.tag_list.serialize_aws_json_1_1(
        value["tags"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AddTagsInput:
    out: AddTagsInput = {}  # type: ignore[typeddict-item]
    if "pipelineId" in data:
        out["pipeline_id"] = data["pipelineId"]
    else:
        raise DeserializationError("AddTagsInput.pipeline_id required")
    if "tags" in data:
        import aws_sdk_data_pipeline.types.tag_list

        out["tags"] = aws_sdk_data_pipeline.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    else:
        raise DeserializationError("AddTagsInput.tags required")
    return out
