"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#AutoTuneOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.auto_tune_desired_state
    import aws_sdk_elasticsearch_service.types.auto_tune_maintenance_schedule_list
    import aws_sdk_elasticsearch_service.types.rollback_on_disable


class AutoTuneOptions(TypedDict):
    desired_state: NotRequired[
        "aws_sdk_elasticsearch_service.types.auto_tune_desired_state.AutoTuneDesiredState"
    ]
    """<p>Specifies the Auto-Tune desired state. Valid values are ENABLED, DISABLED. </p>"""
    rollback_on_disable: NotRequired[
        "aws_sdk_elasticsearch_service.types.rollback_on_disable.RollbackOnDisable"
    ]
    """<p>Specifies the rollback state while disabling Auto-Tune for the domain. Valid values are NO_ROLLBACK, DEFAULT_ROLLBACK. </p>"""
    maintenance_schedules: NotRequired[
        "aws_sdk_elasticsearch_service.types.auto_tune_maintenance_schedule_list.AutoTuneMaintenanceScheduleList"
    ]
    """<p>Specifies list of maitenance schedules. See the <a href=\"https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/auto-tune.html\" target=\"_blank\">Developer Guide</a> for more information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutoTuneOptions) -> dict:
    out: dict = {}
    if "desired_state" in value:
        import aws_sdk_elasticsearch_service.types.auto_tune_desired_state

        out["DesiredState"] = (
            aws_sdk_elasticsearch_service.types.auto_tune_desired_state.serialize_json(
                value["desired_state"]
            )
        )
    if "rollback_on_disable" in value:
        import aws_sdk_elasticsearch_service.types.rollback_on_disable

        out["RollbackOnDisable"] = (
            aws_sdk_elasticsearch_service.types.rollback_on_disable.serialize_json(
                value["rollback_on_disable"]
            )
        )
    if "maintenance_schedules" in value:
        import aws_sdk_elasticsearch_service.types.auto_tune_maintenance_schedule_list

        out["MaintenanceSchedules"] = (
            aws_sdk_elasticsearch_service.types.auto_tune_maintenance_schedule_list.serialize_json(
                value["maintenance_schedules"]
            )
        )
    return out


def deserialize_json(data: dict) -> AutoTuneOptions:
    out: AutoTuneOptions = {}  # type: ignore[typeddict-item]
    if "DesiredState" in data:
        import aws_sdk_elasticsearch_service.types.auto_tune_desired_state

        out["desired_state"] = (
            aws_sdk_elasticsearch_service.types.auto_tune_desired_state.deserialize_json(
                data["DesiredState"]
            )
        )
    if "RollbackOnDisable" in data:
        import aws_sdk_elasticsearch_service.types.rollback_on_disable

        out["rollback_on_disable"] = (
            aws_sdk_elasticsearch_service.types.rollback_on_disable.deserialize_json(
                data["RollbackOnDisable"]
            )
        )
    if "MaintenanceSchedules" in data:
        import aws_sdk_elasticsearch_service.types.auto_tune_maintenance_schedule_list

        out["maintenance_schedules"] = (
            aws_sdk_elasticsearch_service.types.auto_tune_maintenance_schedule_list.deserialize_json(
                data["MaintenanceSchedules"]
            )
        )
    return out
