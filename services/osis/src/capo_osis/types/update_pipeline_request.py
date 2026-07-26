"""Generated from Smithy shape ``com.amazonaws.osis#UpdatePipelineRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_osis.types.buffer_options
    import capo_osis.types.encryption_at_rest_options
    import capo_osis.types.log_publishing_options
    import capo_osis.types.pipeline_configuration_body
    import capo_osis.types.pipeline_name
    import capo_osis.types.pipeline_role_arn
    import capo_osis.types.pipeline_units


class UpdatePipelineRequest(TypedDict, closed=True):
    pipeline_name: "capo_osis.types.pipeline_name.PipelineName"
    """<p>The name of the pipeline to update.</p>"""
    min_units: NotRequired["capo_osis.types.pipeline_units.PipelineUnits"]
    """<p>The minimum pipeline capacity, in Ingestion Compute Units (ICUs).</p>"""
    max_units: NotRequired["capo_osis.types.pipeline_units.PipelineUnits"]
    """<p>The maximum pipeline capacity, in Ingestion Compute Units (ICUs)</p>"""
    pipeline_configuration_body: NotRequired[
        "capo_osis.types.pipeline_configuration_body.PipelineConfigurationBody"
    ]
    r"""<p>The pipeline configuration in YAML format. The command accepts the pipeline configuration as a string or within a .yaml file. If you provide the configuration as a string, each new line must be escaped with <code>\n</code>.</p>"""
    log_publishing_options: NotRequired[
        "capo_osis.types.log_publishing_options.LogPublishingOptions"
    ]
    """<p>Key-value pairs to configure log publishing.</p>"""
    buffer_options: NotRequired["capo_osis.types.buffer_options.BufferOptions"]
    """<p>Key-value pairs to configure persistent buffering for the pipeline.</p>"""
    encryption_at_rest_options: NotRequired[
        "capo_osis.types.encryption_at_rest_options.EncryptionAtRestOptions"
    ]
    """<p>Key-value pairs to configure encryption for data that is written to a persistent buffer.</p>"""
    pipeline_role_arn: NotRequired["capo_osis.types.pipeline_role_arn.PipelineRoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that grants the pipeline permission to access Amazon Web Services resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePipelineRequest) -> dict:
    out: dict = {}
    if "min_units" in value:
        out["MinUnits"] = value["min_units"]
    if "max_units" in value:
        out["MaxUnits"] = value["max_units"]
    if "pipeline_configuration_body" in value:
        out["PipelineConfigurationBody"] = value["pipeline_configuration_body"]
    if "log_publishing_options" in value:
        import capo_osis.types.log_publishing_options

        out["LogPublishingOptions"] = (
            capo_osis.types.log_publishing_options.serialize_json(
                value["log_publishing_options"]
            )
        )
    if "buffer_options" in value:
        import capo_osis.types.buffer_options

        out["BufferOptions"] = capo_osis.types.buffer_options.serialize_json(
            value["buffer_options"]
        )
    if "encryption_at_rest_options" in value:
        import capo_osis.types.encryption_at_rest_options

        out["EncryptionAtRestOptions"] = (
            capo_osis.types.encryption_at_rest_options.serialize_json(
                value["encryption_at_rest_options"]
            )
        )
    if "pipeline_role_arn" in value:
        out["PipelineRoleArn"] = value["pipeline_role_arn"]
    return out


def deserialize_json(data: dict) -> UpdatePipelineRequest:
    out: UpdatePipelineRequest = {}  # type: ignore[typeddict-item]
    if "MinUnits" in data:
        out["min_units"] = data["MinUnits"]
    if "MaxUnits" in data:
        out["max_units"] = data["MaxUnits"]
    if "PipelineConfigurationBody" in data:
        out["pipeline_configuration_body"] = data["PipelineConfigurationBody"]
    if "LogPublishingOptions" in data:
        import capo_osis.types.log_publishing_options

        out["log_publishing_options"] = (
            capo_osis.types.log_publishing_options.deserialize_json(
                data["LogPublishingOptions"]
            )
        )
    if "BufferOptions" in data:
        import capo_osis.types.buffer_options

        out["buffer_options"] = capo_osis.types.buffer_options.deserialize_json(
            data["BufferOptions"]
        )
    if "EncryptionAtRestOptions" in data:
        import capo_osis.types.encryption_at_rest_options

        out["encryption_at_rest_options"] = (
            capo_osis.types.encryption_at_rest_options.deserialize_json(
                data["EncryptionAtRestOptions"]
            )
        )
    if "PipelineRoleArn" in data:
        out["pipeline_role_arn"] = data["PipelineRoleArn"]
    return out
