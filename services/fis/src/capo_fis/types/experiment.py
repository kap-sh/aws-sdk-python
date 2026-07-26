"""Generated from Smithy shape ``com.amazonaws.fis#Experiment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fis.types.creation_time
    import capo_fis.types.experiment_action_map
    import capo_fis.types.experiment_end_time
    import capo_fis.types.experiment_id
    import capo_fis.types.experiment_log_configuration
    import capo_fis.types.experiment_options
    import capo_fis.types.experiment_report
    import capo_fis.types.experiment_report_configuration
    import capo_fis.types.experiment_start_time
    import capo_fis.types.experiment_state
    import capo_fis.types.experiment_stop_condition_list
    import capo_fis.types.experiment_target_map
    import capo_fis.types.experiment_template_id
    import capo_fis.types.resource_arn
    import capo_fis.types.role_arn
    import capo_fis.types.tag_map
    import capo_fis.types.target_account_configurations_count


class Experiment(TypedDict, closed=True):
    id: NotRequired["capo_fis.types.experiment_id.ExperimentId"]
    """<p>The ID of the experiment.</p>"""
    arn: NotRequired["capo_fis.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the experiment.</p>"""
    experiment_template_id: NotRequired[
        "capo_fis.types.experiment_template_id.ExperimentTemplateId"
    ]
    """<p>The ID of the experiment template.</p>"""
    role_arn: NotRequired["capo_fis.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of an IAM role that grants the FIS service permission to perform service actions on your behalf.</p>"""
    state: NotRequired["capo_fis.types.experiment_state.ExperimentState"]
    """<p>The state of the experiment.</p>"""
    targets: NotRequired["capo_fis.types.experiment_target_map.ExperimentTargetMap"]
    """<p>The targets for the experiment.</p>"""
    actions: NotRequired["capo_fis.types.experiment_action_map.ExperimentActionMap"]
    """<p>The actions for the experiment.</p>"""
    stop_conditions: NotRequired[
        "capo_fis.types.experiment_stop_condition_list.ExperimentStopConditionList"
    ]
    """<p>The stop conditions for the experiment.</p>"""
    creation_time: NotRequired["capo_fis.types.creation_time.CreationTime"]
    """<p>The time that the experiment was created.</p>"""
    start_time: NotRequired["capo_fis.types.experiment_start_time.ExperimentStartTime"]
    """<p>The time that the experiment started.</p>"""
    end_time: NotRequired["capo_fis.types.experiment_end_time.ExperimentEndTime"]
    """<p>The time that the experiment ended.</p>"""
    tags: NotRequired["capo_fis.types.tag_map.TagMap"]
    """<p>The tags for the experiment.</p>"""
    log_configuration: NotRequired[
        "capo_fis.types.experiment_log_configuration.ExperimentLogConfiguration"
    ]
    """<p>The configuration for experiment logging.</p>"""
    experiment_options: NotRequired[
        "capo_fis.types.experiment_options.ExperimentOptions"
    ]
    """<p>The experiment options for the experiment.</p>"""
    target_account_configurations_count: NotRequired[
        "capo_fis.types.target_account_configurations_count.TargetAccountConfigurationsCount"
    ]
    """<p>The count of target account configurations for the experiment.</p>"""
    experiment_report_configuration: NotRequired[
        "capo_fis.types.experiment_report_configuration.ExperimentReportConfiguration"
    ]
    """<p>The experiment report configuration for the experiment.</p>"""
    experiment_report: NotRequired["capo_fis.types.experiment_report.ExperimentReport"]
    """<p>The experiment report for the experiment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Experiment) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "experiment_template_id" in value:
        out["experimentTemplateId"] = value["experiment_template_id"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "state" in value:
        import capo_fis.types.experiment_state

        out["state"] = capo_fis.types.experiment_state.serialize_json(value["state"])
    if "targets" in value:
        import capo_fis.types.experiment_target_map

        out["targets"] = capo_fis.types.experiment_target_map.serialize_json(
            value["targets"]
        )
    if "actions" in value:
        import capo_fis.types.experiment_action_map

        out["actions"] = capo_fis.types.experiment_action_map.serialize_json(
            value["actions"]
        )
    if "stop_conditions" in value:
        import capo_fis.types.experiment_stop_condition_list

        out["stopConditions"] = (
            capo_fis.types.experiment_stop_condition_list.serialize_json(
                value["stop_conditions"]
            )
        )
    if "creation_time" in value:
        import capo_fis.types.creation_time

        out["creationTime"] = capo_fis.types.creation_time.serialize_json(
            value["creation_time"]
        )
    if "start_time" in value:
        import capo_fis.types.experiment_start_time

        out["startTime"] = capo_fis.types.experiment_start_time.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_fis.types.experiment_end_time

        out["endTime"] = capo_fis.types.experiment_end_time.serialize_json(
            value["end_time"]
        )
    if "tags" in value:
        import capo_fis.types.tag_map

        out["tags"] = capo_fis.types.tag_map.serialize_json(value["tags"])
    if "log_configuration" in value:
        import capo_fis.types.experiment_log_configuration

        out["logConfiguration"] = (
            capo_fis.types.experiment_log_configuration.serialize_json(
                value["log_configuration"]
            )
        )
    if "experiment_options" in value:
        import capo_fis.types.experiment_options

        out["experimentOptions"] = capo_fis.types.experiment_options.serialize_json(
            value["experiment_options"]
        )
    if "target_account_configurations_count" in value:
        out["targetAccountConfigurationsCount"] = value[
            "target_account_configurations_count"
        ]
    if "experiment_report_configuration" in value:
        import capo_fis.types.experiment_report_configuration

        out["experimentReportConfiguration"] = (
            capo_fis.types.experiment_report_configuration.serialize_json(
                value["experiment_report_configuration"]
            )
        )
    if "experiment_report" in value:
        import capo_fis.types.experiment_report

        out["experimentReport"] = capo_fis.types.experiment_report.serialize_json(
            value["experiment_report"]
        )
    return out


def deserialize_json(data: dict) -> Experiment:
    out: Experiment = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "experimentTemplateId" in data:
        out["experiment_template_id"] = data["experimentTemplateId"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "state" in data:
        import capo_fis.types.experiment_state

        out["state"] = capo_fis.types.experiment_state.deserialize_json(data["state"])
    if "targets" in data:
        import capo_fis.types.experiment_target_map

        out["targets"] = capo_fis.types.experiment_target_map.deserialize_json(
            data["targets"]
        )
    if "actions" in data:
        import capo_fis.types.experiment_action_map

        out["actions"] = capo_fis.types.experiment_action_map.deserialize_json(
            data["actions"]
        )
    if "stopConditions" in data:
        import capo_fis.types.experiment_stop_condition_list

        out["stop_conditions"] = (
            capo_fis.types.experiment_stop_condition_list.deserialize_json(
                data["stopConditions"]
            )
        )
    if "creationTime" in data:
        import capo_fis.types.creation_time

        out["creation_time"] = capo_fis.types.creation_time.deserialize_json(
            data["creationTime"]
        )
    if "startTime" in data:
        import capo_fis.types.experiment_start_time

        out["start_time"] = capo_fis.types.experiment_start_time.deserialize_json(
            data["startTime"]
        )
    if "endTime" in data:
        import capo_fis.types.experiment_end_time

        out["end_time"] = capo_fis.types.experiment_end_time.deserialize_json(
            data["endTime"]
        )
    if "tags" in data:
        import capo_fis.types.tag_map

        out["tags"] = capo_fis.types.tag_map.deserialize_json(data["tags"])
    if "logConfiguration" in data:
        import capo_fis.types.experiment_log_configuration

        out["log_configuration"] = (
            capo_fis.types.experiment_log_configuration.deserialize_json(
                data["logConfiguration"]
            )
        )
    if "experimentOptions" in data:
        import capo_fis.types.experiment_options

        out["experiment_options"] = capo_fis.types.experiment_options.deserialize_json(
            data["experimentOptions"]
        )
    if "targetAccountConfigurationsCount" in data:
        out["target_account_configurations_count"] = data[
            "targetAccountConfigurationsCount"
        ]
    if "experimentReportConfiguration" in data:
        import capo_fis.types.experiment_report_configuration

        out["experiment_report_configuration"] = (
            capo_fis.types.experiment_report_configuration.deserialize_json(
                data["experimentReportConfiguration"]
            )
        )
    if "experimentReport" in data:
        import capo_fis.types.experiment_report

        out["experiment_report"] = capo_fis.types.experiment_report.deserialize_json(
            data["experimentReport"]
        )
    return out
