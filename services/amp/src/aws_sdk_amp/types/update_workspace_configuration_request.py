"""Generated from Smithy shape ``com.amazonaws.amp#UpdateWorkspaceConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_amp.types.idempotency_token
    import aws_sdk_amp.types.limits_per_label_set_list
    import aws_sdk_amp.types.workspace_id


class UpdateWorkspaceConfigurationRequest(TypedDict, closed=True):
    workspace_id: "aws_sdk_amp.types.workspace_id.WorkspaceId"
    r"""<p>The ID of the workspace that you want to update. To find the IDs of your workspaces, use the <a href=\"https://docs.aws.amazon.com/prometheus/latest/APIReference/API_ListWorkspaces.htm\">ListWorkspaces</a> operation.</p>"""
    client_token: NotRequired["aws_sdk_amp.types.idempotency_token.IdempotencyToken"]
    """<p>You can include a token in your operation to make it an idempotent opeartion. </p>"""
    limits_per_label_set: NotRequired[
        "aws_sdk_amp.types.limits_per_label_set_list.LimitsPerLabelSetList"
    ]
    """<p>This is an array of structures, where each structure defines a label set for the workspace, and defines the active time series limit for each of those label sets. Each label name in a label set must be unique.</p>"""
    retention_period_in_days: NotRequired["int"]
    """<p>Specifies how many days that metrics will be retained in the workspace.</p>"""
    out_of_order_time_window_in_seconds: NotRequired["int"]
    """<p>Specifies the time window in seconds for accepting out of order samples. Out of order samples older than this window are rejected.</p>"""
    rule_query_offset_in_seconds: NotRequired["int"]
    """<p>Specifies the duration in seconds to offset rule evaluation queries into the past. This allows ingested samples to be available before rule evaluation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWorkspaceConfigurationRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
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


def deserialize_json(data: dict) -> UpdateWorkspaceConfigurationRequest:
    out: UpdateWorkspaceConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
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
