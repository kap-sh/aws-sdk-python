"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentTemplate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fis.types.creation_time
    import aws_sdk_fis.types.experiment_template_action_map
    import aws_sdk_fis.types.experiment_template_description
    import aws_sdk_fis.types.experiment_template_experiment_options
    import aws_sdk_fis.types.experiment_template_id
    import aws_sdk_fis.types.experiment_template_log_configuration
    import aws_sdk_fis.types.experiment_template_report_configuration
    import aws_sdk_fis.types.experiment_template_stop_condition_list
    import aws_sdk_fis.types.experiment_template_target_map
    import aws_sdk_fis.types.last_update_time
    import aws_sdk_fis.types.resource_arn
    import aws_sdk_fis.types.role_arn
    import aws_sdk_fis.types.tag_map
    import aws_sdk_fis.types.target_account_configurations_count


class ExperimentTemplate(TypedDict, closed=True):
    id: NotRequired["aws_sdk_fis.types.experiment_template_id.ExperimentTemplateId"]
    """<p>The ID of the experiment template.</p>"""
    arn: NotRequired["aws_sdk_fis.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the experiment template.</p>"""
    description: NotRequired[
        "aws_sdk_fis.types.experiment_template_description.ExperimentTemplateDescription"
    ]
    """<p>The description for the experiment template.</p>"""
    targets: NotRequired[
        "aws_sdk_fis.types.experiment_template_target_map.ExperimentTemplateTargetMap"
    ]
    """<p>The targets for the experiment.</p>"""
    actions: NotRequired[
        "aws_sdk_fis.types.experiment_template_action_map.ExperimentTemplateActionMap"
    ]
    """<p>The actions for the experiment.</p>"""
    stop_conditions: NotRequired[
        "aws_sdk_fis.types.experiment_template_stop_condition_list.ExperimentTemplateStopConditionList"
    ]
    """<p>The stop conditions for the experiment.</p>"""
    creation_time: NotRequired["aws_sdk_fis.types.creation_time.CreationTime"]
    """<p>The time the experiment template was created.</p>"""
    last_update_time: NotRequired["aws_sdk_fis.types.last_update_time.LastUpdateTime"]
    """<p>The time the experiment template was last updated.</p>"""
    role_arn: NotRequired["aws_sdk_fis.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of an IAM role.</p>"""
    tags: NotRequired["aws_sdk_fis.types.tag_map.TagMap"]
    """<p>The tags for the experiment template.</p>"""
    log_configuration: NotRequired[
        "aws_sdk_fis.types.experiment_template_log_configuration.ExperimentTemplateLogConfiguration"
    ]
    """<p>The configuration for experiment logging.</p>"""
    experiment_options: NotRequired[
        "aws_sdk_fis.types.experiment_template_experiment_options.ExperimentTemplateExperimentOptions"
    ]
    """<p>The experiment options for an experiment template.</p>"""
    target_account_configurations_count: NotRequired[
        "aws_sdk_fis.types.target_account_configurations_count.TargetAccountConfigurationsCount"
    ]
    """<p>The count of target account configurations for the experiment template.</p>"""
    experiment_report_configuration: NotRequired[
        "aws_sdk_fis.types.experiment_template_report_configuration.ExperimentTemplateReportConfiguration"
    ]
    """<p>Describes the report configuration for the experiment template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentTemplate) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "description" in value:
        out["description"] = value["description"]
    if "targets" in value:
        import aws_sdk_fis.types.experiment_template_target_map

        out["targets"] = (
            aws_sdk_fis.types.experiment_template_target_map.serialize_json(
                value["targets"]
            )
        )
    if "actions" in value:
        import aws_sdk_fis.types.experiment_template_action_map

        out["actions"] = (
            aws_sdk_fis.types.experiment_template_action_map.serialize_json(
                value["actions"]
            )
        )
    if "stop_conditions" in value:
        import aws_sdk_fis.types.experiment_template_stop_condition_list

        out["stopConditions"] = (
            aws_sdk_fis.types.experiment_template_stop_condition_list.serialize_json(
                value["stop_conditions"]
            )
        )
    if "creation_time" in value:
        import aws_sdk_fis.types.creation_time

        out["creationTime"] = aws_sdk_fis.types.creation_time.serialize_json(
            value["creation_time"]
        )
    if "last_update_time" in value:
        import aws_sdk_fis.types.last_update_time

        out["lastUpdateTime"] = aws_sdk_fis.types.last_update_time.serialize_json(
            value["last_update_time"]
        )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "tags" in value:
        import aws_sdk_fis.types.tag_map

        out["tags"] = aws_sdk_fis.types.tag_map.serialize_json(value["tags"])
    if "log_configuration" in value:
        import aws_sdk_fis.types.experiment_template_log_configuration

        out["logConfiguration"] = (
            aws_sdk_fis.types.experiment_template_log_configuration.serialize_json(
                value["log_configuration"]
            )
        )
    if "experiment_options" in value:
        import aws_sdk_fis.types.experiment_template_experiment_options

        out["experimentOptions"] = (
            aws_sdk_fis.types.experiment_template_experiment_options.serialize_json(
                value["experiment_options"]
            )
        )
    if "target_account_configurations_count" in value:
        out["targetAccountConfigurationsCount"] = value[
            "target_account_configurations_count"
        ]
    if "experiment_report_configuration" in value:
        import aws_sdk_fis.types.experiment_template_report_configuration

        out["experimentReportConfiguration"] = (
            aws_sdk_fis.types.experiment_template_report_configuration.serialize_json(
                value["experiment_report_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExperimentTemplate:
    out: ExperimentTemplate = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "description" in data:
        out["description"] = data["description"]
    if "targets" in data:
        import aws_sdk_fis.types.experiment_template_target_map

        out["targets"] = (
            aws_sdk_fis.types.experiment_template_target_map.deserialize_json(
                data["targets"]
            )
        )
    if "actions" in data:
        import aws_sdk_fis.types.experiment_template_action_map

        out["actions"] = (
            aws_sdk_fis.types.experiment_template_action_map.deserialize_json(
                data["actions"]
            )
        )
    if "stopConditions" in data:
        import aws_sdk_fis.types.experiment_template_stop_condition_list

        out["stop_conditions"] = (
            aws_sdk_fis.types.experiment_template_stop_condition_list.deserialize_json(
                data["stopConditions"]
            )
        )
    if "creationTime" in data:
        import aws_sdk_fis.types.creation_time

        out["creation_time"] = aws_sdk_fis.types.creation_time.deserialize_json(
            data["creationTime"]
        )
    if "lastUpdateTime" in data:
        import aws_sdk_fis.types.last_update_time

        out["last_update_time"] = aws_sdk_fis.types.last_update_time.deserialize_json(
            data["lastUpdateTime"]
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "tags" in data:
        import aws_sdk_fis.types.tag_map

        out["tags"] = aws_sdk_fis.types.tag_map.deserialize_json(data["tags"])
    if "logConfiguration" in data:
        import aws_sdk_fis.types.experiment_template_log_configuration

        out["log_configuration"] = (
            aws_sdk_fis.types.experiment_template_log_configuration.deserialize_json(
                data["logConfiguration"]
            )
        )
    if "experimentOptions" in data:
        import aws_sdk_fis.types.experiment_template_experiment_options

        out["experiment_options"] = (
            aws_sdk_fis.types.experiment_template_experiment_options.deserialize_json(
                data["experimentOptions"]
            )
        )
    if "targetAccountConfigurationsCount" in data:
        out["target_account_configurations_count"] = data[
            "targetAccountConfigurationsCount"
        ]
    if "experimentReportConfiguration" in data:
        import aws_sdk_fis.types.experiment_template_report_configuration

        out["experiment_report_configuration"] = (
            aws_sdk_fis.types.experiment_template_report_configuration.deserialize_json(
                data["experimentReportConfiguration"]
            )
        )
    return out
