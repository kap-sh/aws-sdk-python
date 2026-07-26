"""Generated from Smithy shape ``com.amazonaws.iot#AuditMitigationActionsTaskStatistics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.audit_check_name
    import capo_iot.types.task_statistics_for_audit_check

AuditMitigationActionsTaskStatistics: TypeAlias = dict[
    "capo_iot.types.audit_check_name.AuditCheckName",
    "capo_iot.types.task_statistics_for_audit_check.TaskStatisticsForAuditCheck",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AuditMitigationActionsTaskStatistics) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_iot.types.task_statistics_for_audit_check

        out[key] = capo_iot.types.task_statistics_for_audit_check.serialize_json(value)
    return out


def deserialize_json(data: dict) -> AuditMitigationActionsTaskStatistics:
    out: AuditMitigationActionsTaskStatistics = {}
    for key, value in data.items():
        import capo_iot.types.task_statistics_for_audit_check

        out[key] = capo_iot.types.task_statistics_for_audit_check.deserialize_json(
            value
        )
    return out
