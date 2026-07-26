"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrialComponentSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.experiment_entity_name
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.trial_component_arn
    import capo_sagemaker.types.trial_component_source
    import capo_sagemaker.types.trial_component_status
    import capo_sagemaker.types.user_context


class TrialComponentSummary(TypedDict, closed=True):
    trial_component_name: NotRequired[
        "capo_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the trial component.</p>"""
    trial_component_arn: NotRequired[
        "capo_sagemaker.types.trial_component_arn.TrialComponentArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the trial component.</p>"""
    display_name: NotRequired[
        "capo_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the component as displayed. If <code>DisplayName</code> isn't specified, <code>TrialComponentName</code> is displayed.</p>"""
    trial_component_source: NotRequired[
        "capo_sagemaker.types.trial_component_source.TrialComponentSource"
    ]
    status: NotRequired[
        "capo_sagemaker.types.trial_component_status.TrialComponentStatus"
    ]
    """<p>The status of the component. States include:</p> <ul> <li> <p>InProgress</p> </li> <li> <p>Completed</p> </li> <li> <p>Failed</p> </li> </ul>"""
    start_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>When the component started.</p>"""
    end_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>When the component ended.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>When the component was created.</p>"""
    created_by: NotRequired["capo_sagemaker.types.user_context.UserContext"]
    """<p>Who created the trial component.</p>"""
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>When the component was last modified.</p>"""
    last_modified_by: NotRequired["capo_sagemaker.types.user_context.UserContext"]
    """<p>Who last modified the component.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrialComponentSummary) -> dict:
    out: dict = {}
    if "trial_component_name" in value:
        out["TrialComponentName"] = value["trial_component_name"]
    if "trial_component_arn" in value:
        out["TrialComponentArn"] = value["trial_component_arn"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "trial_component_source" in value:
        import capo_sagemaker.types.trial_component_source

        out["TrialComponentSource"] = (
            capo_sagemaker.types.trial_component_source.serialize_aws_json_1_1(
                value["trial_component_source"]
            )
        )
    if "status" in value:
        import capo_sagemaker.types.trial_component_status

        out["Status"] = (
            capo_sagemaker.types.trial_component_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "start_time" in value:
        import capo_sagemaker.types.timestamp

        out["StartTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_sagemaker.types.timestamp

        out["EndTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
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
    return out


def deserialize_aws_json_1_1(data: dict) -> TrialComponentSummary:
    out: TrialComponentSummary = {}  # type: ignore[typeddict-item]
    if "TrialComponentName" in data:
        out["trial_component_name"] = data["TrialComponentName"]
    if "TrialComponentArn" in data:
        out["trial_component_arn"] = data["TrialComponentArn"]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "TrialComponentSource" in data:
        import capo_sagemaker.types.trial_component_source

        out["trial_component_source"] = (
            capo_sagemaker.types.trial_component_source.deserialize_aws_json_1_1(
                data["TrialComponentSource"]
            )
        )
    if "Status" in data:
        import capo_sagemaker.types.trial_component_status

        out["status"] = (
            capo_sagemaker.types.trial_component_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "StartTime" in data:
        import capo_sagemaker.types.timestamp

        out["start_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if "EndTime" in data:
        import capo_sagemaker.types.timestamp

        out["end_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["EndTime"]
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
    return out
