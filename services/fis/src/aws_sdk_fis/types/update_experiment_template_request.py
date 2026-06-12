"""Generated from Smithy shape ``com.amazonaws.fis#UpdateExperimentTemplateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fis.types.experiment_template_description
    import aws_sdk_fis.types.experiment_template_id
    import aws_sdk_fis.types.role_arn
    import aws_sdk_fis.types.update_experiment_template_action_input_map
    import aws_sdk_fis.types.update_experiment_template_experiment_options_input
    import aws_sdk_fis.types.update_experiment_template_log_configuration_input
    import aws_sdk_fis.types.update_experiment_template_report_configuration_input
    import aws_sdk_fis.types.update_experiment_template_stop_condition_input_list
    import aws_sdk_fis.types.update_experiment_template_target_input_map


class UpdateExperimentTemplateRequest(TypedDict):
    id: "aws_sdk_fis.types.experiment_template_id.ExperimentTemplateId"
    """<p>The ID of the experiment template.</p>"""
    description: NotRequired[
        "aws_sdk_fis.types.experiment_template_description.ExperimentTemplateDescription"
    ]
    """<p>A description for the template.</p>"""
    stop_conditions: NotRequired[
        "aws_sdk_fis.types.update_experiment_template_stop_condition_input_list.UpdateExperimentTemplateStopConditionInputList"
    ]
    """<p>The stop conditions for the experiment.</p>"""
    targets: NotRequired[
        "aws_sdk_fis.types.update_experiment_template_target_input_map.UpdateExperimentTemplateTargetInputMap"
    ]
    """<p>The targets for the experiment.</p>"""
    actions: NotRequired[
        "aws_sdk_fis.types.update_experiment_template_action_input_map.UpdateExperimentTemplateActionInputMap"
    ]
    """<p>The actions for the experiment.</p>"""
    role_arn: NotRequired["aws_sdk_fis.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of an IAM role that grants the FIS service permission to perform service actions on your behalf.</p>"""
    log_configuration: NotRequired[
        "aws_sdk_fis.types.update_experiment_template_log_configuration_input.UpdateExperimentTemplateLogConfigurationInput"
    ]
    """<p>The configuration for experiment logging.</p>"""
    experiment_options: NotRequired[
        "aws_sdk_fis.types.update_experiment_template_experiment_options_input.UpdateExperimentTemplateExperimentOptionsInput"
    ]
    """<p>The experiment options for the experiment template.</p>"""
    experiment_report_configuration: NotRequired[
        "aws_sdk_fis.types.update_experiment_template_report_configuration_input.UpdateExperimentTemplateReportConfigurationInput"
    ]
    """<p>The experiment report configuration for the experiment template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateExperimentTemplateRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "stop_conditions" in value:
        import aws_sdk_fis.types.update_experiment_template_stop_condition_input_list

        out["stopConditions"] = (
            aws_sdk_fis.types.update_experiment_template_stop_condition_input_list.serialize_json(
                value["stop_conditions"]
            )
        )
    if "targets" in value:
        import aws_sdk_fis.types.update_experiment_template_target_input_map

        out["targets"] = (
            aws_sdk_fis.types.update_experiment_template_target_input_map.serialize_json(
                value["targets"]
            )
        )
    if "actions" in value:
        import aws_sdk_fis.types.update_experiment_template_action_input_map

        out["actions"] = (
            aws_sdk_fis.types.update_experiment_template_action_input_map.serialize_json(
                value["actions"]
            )
        )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "log_configuration" in value:
        import aws_sdk_fis.types.update_experiment_template_log_configuration_input

        out["logConfiguration"] = (
            aws_sdk_fis.types.update_experiment_template_log_configuration_input.serialize_json(
                value["log_configuration"]
            )
        )
    if "experiment_options" in value:
        import aws_sdk_fis.types.update_experiment_template_experiment_options_input

        out["experimentOptions"] = (
            aws_sdk_fis.types.update_experiment_template_experiment_options_input.serialize_json(
                value["experiment_options"]
            )
        )
    if "experiment_report_configuration" in value:
        import aws_sdk_fis.types.update_experiment_template_report_configuration_input

        out["experimentReportConfiguration"] = (
            aws_sdk_fis.types.update_experiment_template_report_configuration_input.serialize_json(
                value["experiment_report_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateExperimentTemplateRequest:
    out: UpdateExperimentTemplateRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "stopConditions" in data:
        import aws_sdk_fis.types.update_experiment_template_stop_condition_input_list

        out["stop_conditions"] = (
            aws_sdk_fis.types.update_experiment_template_stop_condition_input_list.deserialize_json(
                data["stopConditions"]
            )
        )
    if "targets" in data:
        import aws_sdk_fis.types.update_experiment_template_target_input_map

        out["targets"] = (
            aws_sdk_fis.types.update_experiment_template_target_input_map.deserialize_json(
                data["targets"]
            )
        )
    if "actions" in data:
        import aws_sdk_fis.types.update_experiment_template_action_input_map

        out["actions"] = (
            aws_sdk_fis.types.update_experiment_template_action_input_map.deserialize_json(
                data["actions"]
            )
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "logConfiguration" in data:
        import aws_sdk_fis.types.update_experiment_template_log_configuration_input

        out["log_configuration"] = (
            aws_sdk_fis.types.update_experiment_template_log_configuration_input.deserialize_json(
                data["logConfiguration"]
            )
        )
    if "experimentOptions" in data:
        import aws_sdk_fis.types.update_experiment_template_experiment_options_input

        out["experiment_options"] = (
            aws_sdk_fis.types.update_experiment_template_experiment_options_input.deserialize_json(
                data["experimentOptions"]
            )
        )
    if "experimentReportConfiguration" in data:
        import aws_sdk_fis.types.update_experiment_template_report_configuration_input

        out["experiment_report_configuration"] = (
            aws_sdk_fis.types.update_experiment_template_report_configuration_input.deserialize_json(
                data["experimentReportConfiguration"]
            )
        )
    return out
