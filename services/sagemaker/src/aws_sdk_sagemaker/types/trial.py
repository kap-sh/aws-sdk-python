"""Generated from Smithy shape ``com.amazonaws.sagemaker#Trial``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.experiment_entity_name
    import aws_sdk_sagemaker.types.metadata_properties
    import aws_sdk_sagemaker.types.tag_list
    import aws_sdk_sagemaker.types.timestamp
    import aws_sdk_sagemaker.types.trial_arn
    import aws_sdk_sagemaker.types.trial_component_simple_summaries
    import aws_sdk_sagemaker.types.trial_source
    import aws_sdk_sagemaker.types.user_context


class Trial(TypedDict):
    trial_name: NotRequired[
        "aws_sdk_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the trial.</p>"""
    trial_arn: NotRequired["aws_sdk_sagemaker.types.trial_arn.TrialArn"]
    """<p>The Amazon Resource Name (ARN) of the trial.</p>"""
    display_name: NotRequired[
        "aws_sdk_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the trial as displayed. If <code>DisplayName</code> isn't specified, <code>TrialName</code> is displayed.</p>"""
    experiment_name: NotRequired[
        "aws_sdk_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the experiment the trial is part of.</p>"""
    source: NotRequired["aws_sdk_sagemaker.types.trial_source.TrialSource"]
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>When the trial was created.</p>"""
    created_by: NotRequired["aws_sdk_sagemaker.types.user_context.UserContext"]
    """<p>Who created the trial.</p>"""
    last_modified_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>Who last modified the trial.</p>"""
    last_modified_by: NotRequired["aws_sdk_sagemaker.types.user_context.UserContext"]
    metadata_properties: NotRequired[
        "aws_sdk_sagemaker.types.metadata_properties.MetadataProperties"
    ]
    tags: NotRequired["aws_sdk_sagemaker.types.tag_list.TagList"]
    r"""<p>The list of tags that are associated with the trial. You can use <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html\">Search</a> API to search on the tags.</p>"""
    trial_component_summaries: NotRequired[
        "aws_sdk_sagemaker.types.trial_component_simple_summaries.TrialComponentSimpleSummaries"
    ]
    """<p>A list of the components associated with the trial. For each component, a summary of the component's properties is included.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Trial) -> dict:
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
        import aws_sdk_sagemaker.types.trial_source

        out["Source"] = aws_sdk_sagemaker.types.trial_source.serialize_aws_json_1_1(
            value["source"]
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
    if "metadata_properties" in value:
        import aws_sdk_sagemaker.types.metadata_properties

        out["MetadataProperties"] = (
            aws_sdk_sagemaker.types.metadata_properties.serialize_aws_json_1_1(
                value["metadata_properties"]
            )
        )
    if "tags" in value:
        import aws_sdk_sagemaker.types.tag_list

        out["Tags"] = aws_sdk_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "trial_component_summaries" in value:
        import aws_sdk_sagemaker.types.trial_component_simple_summaries

        out["TrialComponentSummaries"] = (
            aws_sdk_sagemaker.types.trial_component_simple_summaries.serialize_aws_json_1_1(
                value["trial_component_summaries"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Trial:
    out: Trial = {}  # type: ignore[typeddict-item]
    if "TrialName" in data:
        out["trial_name"] = data["TrialName"]
    if "TrialArn" in data:
        out["trial_arn"] = data["TrialArn"]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "ExperimentName" in data:
        out["experiment_name"] = data["ExperimentName"]
    if "Source" in data:
        import aws_sdk_sagemaker.types.trial_source

        out["source"] = aws_sdk_sagemaker.types.trial_source.deserialize_aws_json_1_1(
            data["Source"]
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
    if "MetadataProperties" in data:
        import aws_sdk_sagemaker.types.metadata_properties

        out["metadata_properties"] = (
            aws_sdk_sagemaker.types.metadata_properties.deserialize_aws_json_1_1(
                data["MetadataProperties"]
            )
        )
    if "Tags" in data:
        import aws_sdk_sagemaker.types.tag_list

        out["tags"] = aws_sdk_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "TrialComponentSummaries" in data:
        import aws_sdk_sagemaker.types.trial_component_simple_summaries

        out["trial_component_summaries"] = (
            aws_sdk_sagemaker.types.trial_component_simple_summaries.deserialize_aws_json_1_1(
                data["TrialComponentSummaries"]
            )
        )
    return out
