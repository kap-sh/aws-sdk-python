"""Generated from Smithy shape ``com.amazonaws.datapipeline#PipelineDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_data_pipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_data_pipeline.types.field_list
    import aws_sdk_data_pipeline.types.id
    import aws_sdk_data_pipeline.types.string
    import aws_sdk_data_pipeline.types.tag_list


class PipelineDescription(TypedDict):
    pipeline_id: "aws_sdk_data_pipeline.types.id.id"
    """<p>The pipeline identifier that was assigned by AWS Data Pipeline. This is a string of the form <code>df-297EG78HU43EEXAMPLE</code>.</p>"""
    name: "aws_sdk_data_pipeline.types.id.id"
    """<p>The name of the pipeline.</p>"""
    fields: "aws_sdk_data_pipeline.types.field_list.fieldList"
    """<p>A list of read-only fields that contain metadata about the pipeline: @userId, @accountId, and @pipelineState.</p>"""
    description: NotRequired["aws_sdk_data_pipeline.types.string.string"]
    """<p>Description of the pipeline.</p>"""
    tags: NotRequired["aws_sdk_data_pipeline.types.tag_list.tagList"]
    r"""<p>A list of tags to associated with a pipeline. Tags let you control access to pipelines. For more information, see <a href=\"http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-control-access.html\">Controlling User Access to Pipelines</a> in the <i>AWS Data Pipeline Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineDescription) -> dict:
    out: dict = {}
    out["pipelineId"] = value["pipeline_id"]
    out["name"] = value["name"]
    import aws_sdk_data_pipeline.types.field_list

    out["fields"] = aws_sdk_data_pipeline.types.field_list.serialize_aws_json_1_1(
        value["fields"]
    )
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import aws_sdk_data_pipeline.types.tag_list

        out["tags"] = aws_sdk_data_pipeline.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PipelineDescription:
    out: PipelineDescription = {}  # type: ignore[typeddict-item]
    if "pipelineId" in data:
        out["pipeline_id"] = data["pipelineId"]
    else:
        raise DeserializationError("PipelineDescription.pipeline_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("PipelineDescription.name required")
    if "fields" in data:
        import aws_sdk_data_pipeline.types.field_list

        out["fields"] = aws_sdk_data_pipeline.types.field_list.deserialize_aws_json_1_1(
            data["fields"]
        )
    else:
        raise DeserializationError("PipelineDescription.fields required")
    if "description" in data:
        out["description"] = data["description"]
    if "tags" in data:
        import aws_sdk_data_pipeline.types.tag_list

        out["tags"] = aws_sdk_data_pipeline.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
