"""Generated from Smithy shape ``com.amazonaws.amp#WorkspaceConfigurationDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_amp.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amp.types.limits_per_label_set_list
    import aws_sdk_amp.types.workspace_configuration_status


class WorkspaceConfigurationDescription(TypedDict):
    status: (
        "aws_sdk_amp.types.workspace_configuration_status.WorkspaceConfigurationStatus"
    )
    """<p>This structure displays the current status of the workspace configuration, and might also contain a reason for that status.</p>"""
    limits_per_label_set: NotRequired[
        "aws_sdk_amp.types.limits_per_label_set_list.LimitsPerLabelSetList"
    ]
    """<p>This is an array of structures, where each structure displays one label sets for the workspace and the limits for that label set.</p>"""
    retention_period_in_days: NotRequired["int"]
    """<p>This field displays how many days that metrics are retained in the workspace.</p>"""
    out_of_order_time_window_in_seconds: NotRequired["int"]
    """<p>This field displays the out of order time window in seconds for accepting out of order samples.</p>"""
    rule_query_offset_in_seconds: NotRequired["int"]
    """<p>This field displays the duration in seconds that rule evaluation queries are offset into the past.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkspaceConfigurationDescription) -> dict:
    out: dict = {}
    import aws_sdk_amp.types.workspace_configuration_status

    out["status"] = aws_sdk_amp.types.workspace_configuration_status.serialize_json(
        value["status"]
    )
    if "limits_per_label_set" in value:
        import aws_sdk_amp.types.limits_per_label_set_list

        out["limitsPerLabelSet"] = (
            aws_sdk_amp.types.limits_per_label_set_list.serialize_json(
                value["limits_per_label_set"]
            )
        )
    if "retention_period_in_days" in value:
        out["retentionPeriodInDays"] = value["retention_period_in_days"]
    if "out_of_order_time_window_in_seconds" in value:
        out["outOfOrderTimeWindowInSeconds"] = value[
            "out_of_order_time_window_in_seconds"
        ]
    if "rule_query_offset_in_seconds" in value:
        out["ruleQueryOffsetInSeconds"] = value["rule_query_offset_in_seconds"]
    return out


def deserialize_json(data: dict) -> WorkspaceConfigurationDescription:
    out: WorkspaceConfigurationDescription = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_amp.types.workspace_configuration_status

        out["status"] = (
            aws_sdk_amp.types.workspace_configuration_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("WorkspaceConfigurationDescription.status required")
    if "limitsPerLabelSet" in data:
        import aws_sdk_amp.types.limits_per_label_set_list

        out["limits_per_label_set"] = (
            aws_sdk_amp.types.limits_per_label_set_list.deserialize_json(
                data["limitsPerLabelSet"]
            )
        )
    if "retentionPeriodInDays" in data:
        out["retention_period_in_days"] = data["retentionPeriodInDays"]
    if "outOfOrderTimeWindowInSeconds" in data:
        out["out_of_order_time_window_in_seconds"] = data[
            "outOfOrderTimeWindowInSeconds"
        ]
    if "ruleQueryOffsetInSeconds" in data:
        out["rule_query_offset_in_seconds"] = data["ruleQueryOffsetInSeconds"]
    return out
