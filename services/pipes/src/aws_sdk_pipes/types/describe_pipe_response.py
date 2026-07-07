"""Generated from Smithy shape ``com.amazonaws.pipes#DescribePipeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pipes.types.arn
    import aws_sdk_pipes.types.arn_or_url
    import aws_sdk_pipes.types.kms_key_identifier
    import aws_sdk_pipes.types.optional_arn
    import aws_sdk_pipes.types.pipe_arn
    import aws_sdk_pipes.types.pipe_description
    import aws_sdk_pipes.types.pipe_enrichment_parameters
    import aws_sdk_pipes.types.pipe_log_configuration
    import aws_sdk_pipes.types.pipe_name
    import aws_sdk_pipes.types.pipe_source_parameters
    import aws_sdk_pipes.types.pipe_state
    import aws_sdk_pipes.types.pipe_state_reason
    import aws_sdk_pipes.types.pipe_target_parameters
    import aws_sdk_pipes.types.requested_pipe_state_describe_response
    import aws_sdk_pipes.types.role_arn
    import aws_sdk_pipes.types.tag_map
    import aws_sdk_pipes.types.timestamp


class DescribePipeResponse(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_pipes.types.pipe_arn.PipeArn"]
    """<p>The ARN of the pipe.</p>"""
    name: NotRequired["aws_sdk_pipes.types.pipe_name.PipeName"]
    """<p>The name of the pipe.</p>"""
    description: NotRequired["aws_sdk_pipes.types.pipe_description.PipeDescription"]
    """<p>A description of the pipe.</p>"""
    desired_state: NotRequired[
        "aws_sdk_pipes.types.requested_pipe_state_describe_response.RequestedPipeStateDescribeResponse"
    ]
    """<p>The state the pipe should be in.</p>"""
    current_state: NotRequired["aws_sdk_pipes.types.pipe_state.PipeState"]
    """<p>The state the pipe is in.</p>"""
    state_reason: NotRequired["aws_sdk_pipes.types.pipe_state_reason.PipeStateReason"]
    """<p>The reason the pipe is in its current state.</p>"""
    source: NotRequired["aws_sdk_pipes.types.arn_or_url.ArnOrUrl"]
    """<p>The ARN of the source resource.</p>"""
    source_parameters: NotRequired[
        "aws_sdk_pipes.types.pipe_source_parameters.PipeSourceParameters"
    ]
    """<p>The parameters required to set up a source for your pipe.</p>"""
    enrichment: NotRequired["aws_sdk_pipes.types.optional_arn.OptionalArn"]
    """<p>The ARN of the enrichment resource.</p>"""
    enrichment_parameters: NotRequired[
        "aws_sdk_pipes.types.pipe_enrichment_parameters.PipeEnrichmentParameters"
    ]
    """<p>The parameters required to set up enrichment on your pipe.</p>"""
    target: NotRequired["aws_sdk_pipes.types.arn.Arn"]
    """<p>The ARN of the target resource.</p>"""
    target_parameters: NotRequired[
        "aws_sdk_pipes.types.pipe_target_parameters.PipeTargetParameters"
    ]
    r"""<p>The parameters required to set up a target for your pipe.</p> <p>For more information about pipe target parameters, including how to use dynamic path parameters, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-event-target.html\">Target parameters</a> in the <i>Amazon EventBridge User Guide</i>.</p>"""
    role_arn: NotRequired["aws_sdk_pipes.types.role_arn.RoleArn"]
    """<p>The ARN of the role that allows the pipe to send data to the target.</p>"""
    tags: NotRequired["aws_sdk_pipes.types.tag_map.TagMap"]
    """<p>The list of key-value pairs to associate with the pipe.</p>"""
    creation_time: NotRequired["aws_sdk_pipes.types.timestamp.Timestamp"]
    """<p>The time the pipe was created.</p>"""
    last_modified_time: NotRequired["aws_sdk_pipes.types.timestamp.Timestamp"]
    r"""<p>When the pipe was last updated, in <a href=\"https://www.w3.org/TR/NOTE-datetime\">ISO-8601 format</a> (YYYY-MM-DDThh:mm:ss.sTZD).</p>"""
    log_configuration: NotRequired[
        "aws_sdk_pipes.types.pipe_log_configuration.PipeLogConfiguration"
    ]
    """<p>The logging configuration settings for the pipe.</p>"""
    kms_key_identifier: NotRequired[
        "aws_sdk_pipes.types.kms_key_identifier.KmsKeyIdentifier"
    ]
    r"""<p>The identifier of the KMS customer managed key for EventBridge to use to encrypt pipe data, if one has been specified.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-encryption.html\">Data encryption in EventBridge</a> in the <i>Amazon EventBridge User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribePipeResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "desired_state" in value:
        out["DesiredState"] = value["desired_state"]
    if "current_state" in value:
        out["CurrentState"] = value["current_state"]
    if "state_reason" in value:
        out["StateReason"] = value["state_reason"]
    if "source" in value:
        out["Source"] = value["source"]
    if "source_parameters" in value:
        import aws_sdk_pipes.types.pipe_source_parameters

        out["SourceParameters"] = (
            aws_sdk_pipes.types.pipe_source_parameters.serialize_json(
                value["source_parameters"]
            )
        )
    if "enrichment" in value:
        out["Enrichment"] = value["enrichment"]
    if "enrichment_parameters" in value:
        import aws_sdk_pipes.types.pipe_enrichment_parameters

        out["EnrichmentParameters"] = (
            aws_sdk_pipes.types.pipe_enrichment_parameters.serialize_json(
                value["enrichment_parameters"]
            )
        )
    if "target" in value:
        out["Target"] = value["target"]
    if "target_parameters" in value:
        import aws_sdk_pipes.types.pipe_target_parameters

        out["TargetParameters"] = (
            aws_sdk_pipes.types.pipe_target_parameters.serialize_json(
                value["target_parameters"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "tags" in value:
        import aws_sdk_pipes.types.tag_map

        out["Tags"] = aws_sdk_pipes.types.tag_map.serialize_json(value["tags"])
    if "creation_time" in value:
        import aws_sdk_pipes.types.timestamp

        out["CreationTime"] = aws_sdk_pipes.types.timestamp.serialize_json(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import aws_sdk_pipes.types.timestamp

        out["LastModifiedTime"] = aws_sdk_pipes.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "log_configuration" in value:
        import aws_sdk_pipes.types.pipe_log_configuration

        out["LogConfiguration"] = (
            aws_sdk_pipes.types.pipe_log_configuration.serialize_json(
                value["log_configuration"]
            )
        )
    if "kms_key_identifier" in value:
        out["KmsKeyIdentifier"] = value["kms_key_identifier"]
    return out


def deserialize_json(data: dict) -> DescribePipeResponse:
    out: DescribePipeResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "DesiredState" in data:
        out["desired_state"] = data["DesiredState"]
    if "CurrentState" in data:
        out["current_state"] = data["CurrentState"]
    if "StateReason" in data:
        out["state_reason"] = data["StateReason"]
    if "Source" in data:
        out["source"] = data["Source"]
    if "SourceParameters" in data:
        import aws_sdk_pipes.types.pipe_source_parameters

        out["source_parameters"] = (
            aws_sdk_pipes.types.pipe_source_parameters.deserialize_json(
                data["SourceParameters"]
            )
        )
    if "Enrichment" in data:
        out["enrichment"] = data["Enrichment"]
    if "EnrichmentParameters" in data:
        import aws_sdk_pipes.types.pipe_enrichment_parameters

        out["enrichment_parameters"] = (
            aws_sdk_pipes.types.pipe_enrichment_parameters.deserialize_json(
                data["EnrichmentParameters"]
            )
        )
    if "Target" in data:
        out["target"] = data["Target"]
    if "TargetParameters" in data:
        import aws_sdk_pipes.types.pipe_target_parameters

        out["target_parameters"] = (
            aws_sdk_pipes.types.pipe_target_parameters.deserialize_json(
                data["TargetParameters"]
            )
        )
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "Tags" in data:
        import aws_sdk_pipes.types.tag_map

        out["tags"] = aws_sdk_pipes.types.tag_map.deserialize_json(data["Tags"])
    if "CreationTime" in data:
        import aws_sdk_pipes.types.timestamp

        out["creation_time"] = aws_sdk_pipes.types.timestamp.deserialize_json(
            data["CreationTime"]
        )
    if "LastModifiedTime" in data:
        import aws_sdk_pipes.types.timestamp

        out["last_modified_time"] = aws_sdk_pipes.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    if "LogConfiguration" in data:
        import aws_sdk_pipes.types.pipe_log_configuration

        out["log_configuration"] = (
            aws_sdk_pipes.types.pipe_log_configuration.deserialize_json(
                data["LogConfiguration"]
            )
        )
    if "KmsKeyIdentifier" in data:
        out["kms_key_identifier"] = data["KmsKeyIdentifier"]
    return out
