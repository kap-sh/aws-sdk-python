"""Generated from Smithy shape ``com.amazonaws.datapipeline#RemoveTagsInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_data_pipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_data_pipeline.types.id
    import aws_sdk_data_pipeline.types.string_list


class RemoveTagsInput(TypedDict):
    pipeline_id: "aws_sdk_data_pipeline.types.id.id"
    """<p>The ID of the pipeline.</p>"""
    tag_keys: "aws_sdk_data_pipeline.types.string_list.stringList"
    """<p>The keys of the tags to remove.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoveTagsInput) -> dict:
    out: dict = {}
    out["pipelineId"] = value["pipeline_id"]
    import aws_sdk_data_pipeline.types.string_list

    out["tagKeys"] = aws_sdk_data_pipeline.types.string_list.serialize_aws_json_1_1(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RemoveTagsInput:
    out: RemoveTagsInput = {}  # type: ignore[typeddict-item]
    if "pipelineId" in data:
        out["pipeline_id"] = data["pipelineId"]
    else:
        raise DeserializationError("RemoveTagsInput.pipeline_id required")
    if "tagKeys" in data:
        import aws_sdk_data_pipeline.types.string_list

        out["tag_keys"] = (
            aws_sdk_data_pipeline.types.string_list.deserialize_aws_json_1_1(
                data["tagKeys"]
            )
        )
    else:
        raise DeserializationError("RemoveTagsInput.tag_keys required")
    return out
