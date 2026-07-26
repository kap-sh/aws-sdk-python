"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrialComponentSimpleSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.experiment_entity_name
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.trial_component_arn
    import capo_sagemaker.types.trial_component_source
    import capo_sagemaker.types.user_context


class TrialComponentSimpleSummary(TypedDict, closed=True):
    trial_component_name: NotRequired[
        "capo_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the trial component.</p>"""
    trial_component_arn: NotRequired[
        "capo_sagemaker.types.trial_component_arn.TrialComponentArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the trial component.</p>"""
    trial_component_source: NotRequired[
        "capo_sagemaker.types.trial_component_source.TrialComponentSource"
    ]
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>When the component was created.</p>"""
    created_by: NotRequired["capo_sagemaker.types.user_context.UserContext"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrialComponentSimpleSummary) -> dict:
    out: dict = {}
    if "trial_component_name" in value:
        out["TrialComponentName"] = value["trial_component_name"]
    if "trial_component_arn" in value:
        out["TrialComponentArn"] = value["trial_component_arn"]
    if "trial_component_source" in value:
        import capo_sagemaker.types.trial_component_source

        out["TrialComponentSource"] = (
            capo_sagemaker.types.trial_component_source.serialize_aws_json_1_1(
                value["trial_component_source"]
            )
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
    return out


def deserialize_aws_json_1_1(data: dict) -> TrialComponentSimpleSummary:
    out: TrialComponentSimpleSummary = {}  # type: ignore[typeddict-item]
    if "TrialComponentName" in data:
        out["trial_component_name"] = data["TrialComponentName"]
    if "TrialComponentArn" in data:
        out["trial_component_arn"] = data["TrialComponentArn"]
    if "TrialComponentSource" in data:
        import capo_sagemaker.types.trial_component_source

        out["trial_component_source"] = (
            capo_sagemaker.types.trial_component_source.deserialize_aws_json_1_1(
                data["TrialComponentSource"]
            )
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
    return out
