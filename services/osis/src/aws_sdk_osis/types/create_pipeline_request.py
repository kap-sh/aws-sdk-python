"""Generated from Smithy shape ``com.amazonaws.osis#CreatePipelineRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_osis.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_osis.types.buffer_options
    import aws_sdk_osis.types.encryption_at_rest_options
    import aws_sdk_osis.types.log_publishing_options
    import aws_sdk_osis.types.pipeline_configuration_body
    import aws_sdk_osis.types.pipeline_name
    import aws_sdk_osis.types.pipeline_role_arn
    import aws_sdk_osis.types.pipeline_units
    import aws_sdk_osis.types.tag_list
    import aws_sdk_osis.types.vpc_options


class CreatePipelineRequest(TypedDict):
    pipeline_name: "aws_sdk_osis.types.pipeline_name.PipelineName"
    """<p>The name of the OpenSearch Ingestion pipeline to create. Pipeline names are unique across the pipelines owned by an account within an Amazon Web Services Region.</p>"""
    min_units: "aws_sdk_osis.types.pipeline_units.PipelineUnits"
    """<p>The minimum pipeline capacity, in Ingestion Compute Units (ICUs).</p>"""
    max_units: "aws_sdk_osis.types.pipeline_units.PipelineUnits"
    """<p>The maximum pipeline capacity, in Ingestion Compute Units (ICUs).</p>"""
    pipeline_configuration_body: (
        "aws_sdk_osis.types.pipeline_configuration_body.PipelineConfigurationBody"
    )
    """<p>The pipeline configuration in YAML format. The command accepts the pipeline configuration as a string or within a .yaml file. If you provide the configuration as a string, each new line must be escaped with <code>\n</code>.</p>"""
    log_publishing_options: NotRequired[
        "aws_sdk_osis.types.log_publishing_options.LogPublishingOptions"
    ]
    """<p>Key-value pairs to configure log publishing.</p>"""
    vpc_options: NotRequired["aws_sdk_osis.types.vpc_options.VpcOptions"]
    """<p>Container for the values required to configure VPC access for the pipeline. If you don't specify these values, OpenSearch Ingestion creates the pipeline with a public endpoint.</p>"""
    buffer_options: NotRequired["aws_sdk_osis.types.buffer_options.BufferOptions"]
    """<p>Key-value pairs to configure persistent buffering for the pipeline.</p>"""
    encryption_at_rest_options: NotRequired[
        "aws_sdk_osis.types.encryption_at_rest_options.EncryptionAtRestOptions"
    ]
    """<p>Key-value pairs to configure encryption for data that is written to a persistent buffer.</p>"""
    tags: NotRequired["aws_sdk_osis.types.tag_list.TagList"]
    """<p>List of tags to add to the pipeline upon creation.</p>"""
    pipeline_role_arn: NotRequired[
        "aws_sdk_osis.types.pipeline_role_arn.PipelineRoleArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the IAM role that grants the pipeline permission to access Amazon Web Services resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePipelineRequest) -> dict:
    out: dict = {}
    out["PipelineName"] = value["pipeline_name"]
    out["MinUnits"] = value["min_units"]
    out["MaxUnits"] = value["max_units"]
    out["PipelineConfigurationBody"] = value["pipeline_configuration_body"]
    if "log_publishing_options" in value:
        import aws_sdk_osis.types.log_publishing_options

        out["LogPublishingOptions"] = (
            aws_sdk_osis.types.log_publishing_options.serialize_json(
                value["log_publishing_options"]
            )
        )
    if "vpc_options" in value:
        import aws_sdk_osis.types.vpc_options

        out["VpcOptions"] = aws_sdk_osis.types.vpc_options.serialize_json(
            value["vpc_options"]
        )
    if "buffer_options" in value:
        import aws_sdk_osis.types.buffer_options

        out["BufferOptions"] = aws_sdk_osis.types.buffer_options.serialize_json(
            value["buffer_options"]
        )
    if "encryption_at_rest_options" in value:
        import aws_sdk_osis.types.encryption_at_rest_options

        out["EncryptionAtRestOptions"] = (
            aws_sdk_osis.types.encryption_at_rest_options.serialize_json(
                value["encryption_at_rest_options"]
            )
        )
    if "tags" in value:
        import aws_sdk_osis.types.tag_list

        out["Tags"] = aws_sdk_osis.types.tag_list.serialize_json(value["tags"])
    if "pipeline_role_arn" in value:
        out["PipelineRoleArn"] = value["pipeline_role_arn"]
    return out


def deserialize_json(data: dict) -> CreatePipelineRequest:
    out: CreatePipelineRequest = {}  # type: ignore[typeddict-item]
    if "PipelineName" in data:
        out["pipeline_name"] = data["PipelineName"]
    else:
        raise DeserializationError("CreatePipelineRequest.pipeline_name required")
    if "MinUnits" in data:
        out["min_units"] = data["MinUnits"]
    else:
        raise DeserializationError("CreatePipelineRequest.min_units required")
    if "MaxUnits" in data:
        out["max_units"] = data["MaxUnits"]
    else:
        raise DeserializationError("CreatePipelineRequest.max_units required")
    if "PipelineConfigurationBody" in data:
        out["pipeline_configuration_body"] = data["PipelineConfigurationBody"]
    else:
        raise DeserializationError(
            "CreatePipelineRequest.pipeline_configuration_body required"
        )
    if "LogPublishingOptions" in data:
        import aws_sdk_osis.types.log_publishing_options

        out["log_publishing_options"] = (
            aws_sdk_osis.types.log_publishing_options.deserialize_json(
                data["LogPublishingOptions"]
            )
        )
    if "VpcOptions" in data:
        import aws_sdk_osis.types.vpc_options

        out["vpc_options"] = aws_sdk_osis.types.vpc_options.deserialize_json(
            data["VpcOptions"]
        )
    if "BufferOptions" in data:
        import aws_sdk_osis.types.buffer_options

        out["buffer_options"] = aws_sdk_osis.types.buffer_options.deserialize_json(
            data["BufferOptions"]
        )
    if "EncryptionAtRestOptions" in data:
        import aws_sdk_osis.types.encryption_at_rest_options

        out["encryption_at_rest_options"] = (
            aws_sdk_osis.types.encryption_at_rest_options.deserialize_json(
                data["EncryptionAtRestOptions"]
            )
        )
    if "Tags" in data:
        import aws_sdk_osis.types.tag_list

        out["tags"] = aws_sdk_osis.types.tag_list.deserialize_json(data["Tags"])
    if "PipelineRoleArn" in data:
        out["pipeline_role_arn"] = data["PipelineRoleArn"]
    return out
