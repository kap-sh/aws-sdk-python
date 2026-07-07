"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeTrialComponentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.experiment_entity_name
    import aws_sdk_sagemaker.types.lineage_group_arn
    import aws_sdk_sagemaker.types.metadata_properties
    import aws_sdk_sagemaker.types.timestamp
    import aws_sdk_sagemaker.types.trial_component_arn
    import aws_sdk_sagemaker.types.trial_component_artifacts
    import aws_sdk_sagemaker.types.trial_component_metric_summaries
    import aws_sdk_sagemaker.types.trial_component_parameters
    import aws_sdk_sagemaker.types.trial_component_source
    import aws_sdk_sagemaker.types.trial_component_sources
    import aws_sdk_sagemaker.types.trial_component_status
    import aws_sdk_sagemaker.types.user_context


class DescribeTrialComponentResponse(TypedDict, closed=True):
    trial_component_name: NotRequired[
        "aws_sdk_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the trial component.</p>"""
    trial_component_arn: NotRequired[
        "aws_sdk_sagemaker.types.trial_component_arn.TrialComponentArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the trial component.</p>"""
    display_name: NotRequired[
        "aws_sdk_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the component as displayed. If <code>DisplayName</code> isn't specified, <code>TrialComponentName</code> is displayed.</p>"""
    source: NotRequired[
        "aws_sdk_sagemaker.types.trial_component_source.TrialComponentSource"
    ]
    """<p>The Amazon Resource Name (ARN) of the source and, optionally, the job type.</p>"""
    status: NotRequired[
        "aws_sdk_sagemaker.types.trial_component_status.TrialComponentStatus"
    ]
    """<p>The status of the component. States include:</p> <ul> <li> <p>InProgress</p> </li> <li> <p>Completed</p> </li> <li> <p>Failed</p> </li> </ul>"""
    start_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>When the component started.</p>"""
    end_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>When the component ended.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>When the component was created.</p>"""
    created_by: NotRequired["aws_sdk_sagemaker.types.user_context.UserContext"]
    """<p>Who created the trial component.</p>"""
    last_modified_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>When the component was last modified.</p>"""
    last_modified_by: NotRequired["aws_sdk_sagemaker.types.user_context.UserContext"]
    """<p>Who last modified the component.</p>"""
    parameters: NotRequired[
        "aws_sdk_sagemaker.types.trial_component_parameters.TrialComponentParameters"
    ]
    """<p>The hyperparameters of the component.</p>"""
    input_artifacts: NotRequired[
        "aws_sdk_sagemaker.types.trial_component_artifacts.TrialComponentArtifacts"
    ]
    """<p>The input artifacts of the component.</p>"""
    output_artifacts: NotRequired[
        "aws_sdk_sagemaker.types.trial_component_artifacts.TrialComponentArtifacts"
    ]
    """<p>The output artifacts of the component.</p>"""
    metadata_properties: NotRequired[
        "aws_sdk_sagemaker.types.metadata_properties.MetadataProperties"
    ]
    metrics: NotRequired[
        "aws_sdk_sagemaker.types.trial_component_metric_summaries.TrialComponentMetricSummaries"
    ]
    """<p>The metrics for the component.</p>"""
    lineage_group_arn: NotRequired[
        "aws_sdk_sagemaker.types.lineage_group_arn.LineageGroupArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the lineage group.</p>"""
    sources: NotRequired[
        "aws_sdk_sagemaker.types.trial_component_sources.TrialComponentSources"
    ]
    """<p>A list of ARNs and, if applicable, job types for multiple sources of an experiment run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTrialComponentResponse) -> dict:
    out: dict = {}
    if "trial_component_name" in value:
        out["TrialComponentName"] = value["trial_component_name"]
    if "trial_component_arn" in value:
        out["TrialComponentArn"] = value["trial_component_arn"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "source" in value:
        import aws_sdk_sagemaker.types.trial_component_source

        out["Source"] = (
            aws_sdk_sagemaker.types.trial_component_source.serialize_aws_json_1_1(
                value["source"]
            )
        )
    if "status" in value:
        import aws_sdk_sagemaker.types.trial_component_status

        out["Status"] = (
            aws_sdk_sagemaker.types.trial_component_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "start_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["StartTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["EndTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "created_by" in value:
        import aws_sdk_sagemaker.types.user_context

        out["CreatedBy"] = aws_sdk_sagemaker.types.user_context.serialize_aws_json_1_1(
            value["created_by"]
        )
    if "last_modified_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["LastModifiedTime"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "last_modified_by" in value:
        import aws_sdk_sagemaker.types.user_context

        out["LastModifiedBy"] = (
            aws_sdk_sagemaker.types.user_context.serialize_aws_json_1_1(
                value["last_modified_by"]
            )
        )
    if "parameters" in value:
        import aws_sdk_sagemaker.types.trial_component_parameters

        out["Parameters"] = (
            aws_sdk_sagemaker.types.trial_component_parameters.serialize_aws_json_1_1(
                value["parameters"]
            )
        )
    if "input_artifacts" in value:
        import aws_sdk_sagemaker.types.trial_component_artifacts

        out["InputArtifacts"] = (
            aws_sdk_sagemaker.types.trial_component_artifacts.serialize_aws_json_1_1(
                value["input_artifacts"]
            )
        )
    if "output_artifacts" in value:
        import aws_sdk_sagemaker.types.trial_component_artifacts

        out["OutputArtifacts"] = (
            aws_sdk_sagemaker.types.trial_component_artifacts.serialize_aws_json_1_1(
                value["output_artifacts"]
            )
        )
    if "metadata_properties" in value:
        import aws_sdk_sagemaker.types.metadata_properties

        out["MetadataProperties"] = (
            aws_sdk_sagemaker.types.metadata_properties.serialize_aws_json_1_1(
                value["metadata_properties"]
            )
        )
    if "metrics" in value:
        import aws_sdk_sagemaker.types.trial_component_metric_summaries

        out["Metrics"] = (
            aws_sdk_sagemaker.types.trial_component_metric_summaries.serialize_aws_json_1_1(
                value["metrics"]
            )
        )
    if "lineage_group_arn" in value:
        out["LineageGroupArn"] = value["lineage_group_arn"]
    if "sources" in value:
        import aws_sdk_sagemaker.types.trial_component_sources

        out["Sources"] = (
            aws_sdk_sagemaker.types.trial_component_sources.serialize_aws_json_1_1(
                value["sources"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTrialComponentResponse:
    out: DescribeTrialComponentResponse = {}  # type: ignore[typeddict-item]
    if "TrialComponentName" in data:
        out["trial_component_name"] = data["TrialComponentName"]
    if "TrialComponentArn" in data:
        out["trial_component_arn"] = data["TrialComponentArn"]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "Source" in data:
        import aws_sdk_sagemaker.types.trial_component_source

        out["source"] = (
            aws_sdk_sagemaker.types.trial_component_source.deserialize_aws_json_1_1(
                data["Source"]
            )
        )
    if "Status" in data:
        import aws_sdk_sagemaker.types.trial_component_status

        out["status"] = (
            aws_sdk_sagemaker.types.trial_component_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "StartTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["start_time"] = aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if "EndTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["end_time"] = aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "CreatedBy" in data:
        import aws_sdk_sagemaker.types.user_context

        out["created_by"] = (
            aws_sdk_sagemaker.types.user_context.deserialize_aws_json_1_1(
                data["CreatedBy"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["last_modified_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "LastModifiedBy" in data:
        import aws_sdk_sagemaker.types.user_context

        out["last_modified_by"] = (
            aws_sdk_sagemaker.types.user_context.deserialize_aws_json_1_1(
                data["LastModifiedBy"]
            )
        )
    if "Parameters" in data:
        import aws_sdk_sagemaker.types.trial_component_parameters

        out["parameters"] = (
            aws_sdk_sagemaker.types.trial_component_parameters.deserialize_aws_json_1_1(
                data["Parameters"]
            )
        )
    if "InputArtifacts" in data:
        import aws_sdk_sagemaker.types.trial_component_artifacts

        out["input_artifacts"] = (
            aws_sdk_sagemaker.types.trial_component_artifacts.deserialize_aws_json_1_1(
                data["InputArtifacts"]
            )
        )
    if "OutputArtifacts" in data:
        import aws_sdk_sagemaker.types.trial_component_artifacts

        out["output_artifacts"] = (
            aws_sdk_sagemaker.types.trial_component_artifacts.deserialize_aws_json_1_1(
                data["OutputArtifacts"]
            )
        )
    if "MetadataProperties" in data:
        import aws_sdk_sagemaker.types.metadata_properties

        out["metadata_properties"] = (
            aws_sdk_sagemaker.types.metadata_properties.deserialize_aws_json_1_1(
                data["MetadataProperties"]
            )
        )
    if "Metrics" in data:
        import aws_sdk_sagemaker.types.trial_component_metric_summaries

        out["metrics"] = (
            aws_sdk_sagemaker.types.trial_component_metric_summaries.deserialize_aws_json_1_1(
                data["Metrics"]
            )
        )
    if "LineageGroupArn" in data:
        out["lineage_group_arn"] = data["LineageGroupArn"]
    if "Sources" in data:
        import aws_sdk_sagemaker.types.trial_component_sources

        out["sources"] = (
            aws_sdk_sagemaker.types.trial_component_sources.deserialize_aws_json_1_1(
                data["Sources"]
            )
        )
    return out
