"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeTrialResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.experiment_entity_name
    import capo_sagemaker.types.metadata_properties
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.trial_arn
    import capo_sagemaker.types.trial_source
    import capo_sagemaker.types.user_context


class DescribeTrialResponse(TypedDict, closed=True):
    trial_name: NotRequired[
        "capo_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the trial.</p>"""
    trial_arn: NotRequired["capo_sagemaker.types.trial_arn.TrialArn"]
    """<p>The Amazon Resource Name (ARN) of the trial.</p>"""
    display_name: NotRequired[
        "capo_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the trial as displayed. If <code>DisplayName</code> isn't specified, <code>TrialName</code> is displayed.</p>"""
    experiment_name: NotRequired[
        "capo_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the experiment the trial is part of.</p>"""
    source: NotRequired["capo_sagemaker.types.trial_source.TrialSource"]
    """<p>The Amazon Resource Name (ARN) of the source and, optionally, the job type.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>When the trial was created.</p>"""
    created_by: NotRequired["capo_sagemaker.types.user_context.UserContext"]
    """<p>Who created the trial.</p>"""
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>When the trial was last modified.</p>"""
    last_modified_by: NotRequired["capo_sagemaker.types.user_context.UserContext"]
    """<p>Who last modified the trial.</p>"""
    metadata_properties: NotRequired[
        "capo_sagemaker.types.metadata_properties.MetadataProperties"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTrialResponse) -> dict:
    out: dict = {}
    if "trial_name" in value:
        out["TrialName"] = value["trial_name"]
    if "trial_arn" in value:
        out["TrialArn"] = value["trial_arn"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "experiment_name" in value:
        out["ExperimentName"] = value["experiment_name"]
    if "source" in value:
        import capo_sagemaker.types.trial_source

        out["Source"] = capo_sagemaker.types.trial_source.serialize_aws_json_1_1(
            value["source"]
        )
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "created_by" in value:
        import capo_sagemaker.types.user_context

        out["CreatedBy"] = capo_sagemaker.types.user_context.serialize_aws_json_1_1(
            value["created_by"]
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.timestamp

        out["LastModifiedTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_time"]
        )
    if "last_modified_by" in value:
        import capo_sagemaker.types.user_context

        out["LastModifiedBy"] = (
            capo_sagemaker.types.user_context.serialize_aws_json_1_1(
                value["last_modified_by"]
            )
        )
    if "metadata_properties" in value:
        import capo_sagemaker.types.metadata_properties

        out["MetadataProperties"] = (
            capo_sagemaker.types.metadata_properties.serialize_aws_json_1_1(
                value["metadata_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTrialResponse:
    out: DescribeTrialResponse = {}  # type: ignore[typeddict-item]
    if "TrialName" in data:
        out["trial_name"] = data["TrialName"]
    if "TrialArn" in data:
        out["trial_arn"] = data["TrialArn"]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "ExperimentName" in data:
        out["experiment_name"] = data["ExperimentName"]
    if "Source" in data:
        import capo_sagemaker.types.trial_source

        out["source"] = capo_sagemaker.types.trial_source.deserialize_aws_json_1_1(
            data["Source"]
        )
    if "CreationTime" in data:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "CreatedBy" in data:
        import capo_sagemaker.types.user_context

        out["created_by"] = capo_sagemaker.types.user_context.deserialize_aws_json_1_1(
            data["CreatedBy"]
        )
    if "LastModifiedTime" in data:
        import capo_sagemaker.types.timestamp

        out["last_modified_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "LastModifiedBy" in data:
        import capo_sagemaker.types.user_context

        out["last_modified_by"] = (
            capo_sagemaker.types.user_context.deserialize_aws_json_1_1(
                data["LastModifiedBy"]
            )
        )
    if "MetadataProperties" in data:
        import capo_sagemaker.types.metadata_properties

        out["metadata_properties"] = (
            capo_sagemaker.types.metadata_properties.deserialize_aws_json_1_1(
                data["MetadataProperties"]
            )
        )
    return out
