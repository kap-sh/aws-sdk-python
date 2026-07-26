"""Generated from Smithy shape ``com.amazonaws.cloudwatch#CompositeAlarm``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.actions_enabled
    import capo_cloudwatch.types.actions_suppressed_by
    import capo_cloudwatch.types.actions_suppressed_reason
    import capo_cloudwatch.types.alarm_arn
    import capo_cloudwatch.types.alarm_description
    import capo_cloudwatch.types.alarm_name
    import capo_cloudwatch.types.alarm_rule
    import capo_cloudwatch.types.resource_list
    import capo_cloudwatch.types.state_reason
    import capo_cloudwatch.types.state_reason_data
    import capo_cloudwatch.types.state_value
    import capo_cloudwatch.types.suppressor_period
    import capo_cloudwatch.types.timestamp


class CompositeAlarm(TypedDict, closed=True):
    actions_enabled: NotRequired["capo_cloudwatch.types.actions_enabled.ActionsEnabled"]
    """<p>Indicates whether actions should be executed during any changes to the alarm state.</p>"""
    alarm_actions: NotRequired["capo_cloudwatch.types.resource_list.ResourceList"]
    """<p>The actions to execute when this alarm transitions to the ALARM state from any other state. Each action is specified as an Amazon Resource Name (ARN).</p>"""
    alarm_arn: NotRequired["capo_cloudwatch.types.alarm_arn.AlarmArn"]
    """<p>The Amazon Resource Name (ARN) of the alarm.</p>"""
    alarm_configuration_updated_timestamp: NotRequired[
        "capo_cloudwatch.types.timestamp.Timestamp"
    ]
    """<p>The time stamp of the last update to the alarm configuration.</p>"""
    alarm_description: NotRequired[
        "capo_cloudwatch.types.alarm_description.AlarmDescription"
    ]
    """<p>The description of the alarm.</p>"""
    alarm_name: NotRequired["capo_cloudwatch.types.alarm_name.AlarmName"]
    """<p>The name of the alarm.</p>"""
    alarm_rule: NotRequired["capo_cloudwatch.types.alarm_rule.AlarmRule"]
    """<p>The rule that this alarm uses to evaluate its alarm state.</p>"""
    insufficient_data_actions: NotRequired[
        "capo_cloudwatch.types.resource_list.ResourceList"
    ]
    """<p>The actions to execute when this alarm transitions to the INSUFFICIENT_DATA state from any other state. Each action is specified as an Amazon Resource Name (ARN).</p>"""
    ok_actions: NotRequired["capo_cloudwatch.types.resource_list.ResourceList"]
    """<p>The actions to execute when this alarm transitions to the OK state from any other state. Each action is specified as an Amazon Resource Name (ARN).</p>"""
    state_reason: NotRequired["capo_cloudwatch.types.state_reason.StateReason"]
    """<p>An explanation for the alarm state, in text format.</p>"""
    state_reason_data: NotRequired[
        "capo_cloudwatch.types.state_reason_data.StateReasonData"
    ]
    """<p>An explanation for the alarm state, in JSON format.</p>"""
    state_updated_timestamp: NotRequired["capo_cloudwatch.types.timestamp.Timestamp"]
    """<p>Tracks the timestamp of any state update, even if <code>StateValue</code> doesn't change.</p>"""
    state_value: NotRequired["capo_cloudwatch.types.state_value.StateValue"]
    """<p>The state value for the alarm.</p>"""
    state_transitioned_timestamp: NotRequired[
        "capo_cloudwatch.types.timestamp.Timestamp"
    ]
    """<p> The timestamp of the last change to the alarm's <code>StateValue</code>. </p>"""
    actions_suppressed_by: NotRequired[
        "capo_cloudwatch.types.actions_suppressed_by.ActionsSuppressedBy"
    ]
    """<p> When the value is <code>ALARM</code>, it means that the actions are suppressed because the suppressor alarm is in <code>ALARM</code> When the value is <code>WaitPeriod</code>, it means that the actions are suppressed because the composite alarm is waiting for the suppressor alarm to go into into the <code>ALARM</code> state. The maximum waiting time is as specified in <code>ActionsSuppressorWaitPeriod</code>. After this time, the composite alarm performs its actions. When the value is <code>ExtensionPeriod</code>, it means that the actions are suppressed because the composite alarm is waiting after the suppressor alarm went out of the <code>ALARM</code> state. The maximum waiting time is as specified in <code>ActionsSuppressorExtensionPeriod</code>. After this time, the composite alarm performs its actions. </p>"""
    actions_suppressed_reason: NotRequired[
        "capo_cloudwatch.types.actions_suppressed_reason.ActionsSuppressedReason"
    ]
    """<p> Captures the reason for action suppression. </p>"""
    actions_suppressor: NotRequired["capo_cloudwatch.types.alarm_arn.AlarmArn"]
    """<p> Actions will be suppressed if the suppressor alarm is in the <code>ALARM</code> state. <code>ActionsSuppressor</code> can be an AlarmName or an Amazon Resource Name (ARN) from an existing alarm. </p>"""
    actions_suppressor_wait_period: NotRequired[
        "capo_cloudwatch.types.suppressor_period.SuppressorPeriod"
    ]
    """<p> The maximum time in seconds that the composite alarm waits for the suppressor alarm to go into the <code>ALARM</code> state. After this time, the composite alarm performs its actions. </p> <important> <p> <code>WaitPeriod</code> is required only when <code>ActionsSuppressor</code> is specified. </p> </important>"""
    actions_suppressor_extension_period: NotRequired[
        "capo_cloudwatch.types.suppressor_period.SuppressorPeriod"
    ]
    """<p> The maximum time in seconds that the composite alarm waits after suppressor alarm goes out of the <code>ALARM</code> state. After this time, the composite alarm performs its actions. </p> <important> <p> <code>ExtensionPeriod</code> is required only when <code>ActionsSuppressor</code> is specified. </p> </important>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CompositeAlarm) -> dict:
    out: dict = {}
    if "actions_enabled" in value:
        out["ActionsEnabled"] = value["actions_enabled"]
    if "alarm_actions" in value:
        import capo_cloudwatch.types.resource_list

        out["AlarmActions"] = (
            capo_cloudwatch.types.resource_list.serialize_aws_json_1_0(
                value["alarm_actions"]
            )
        )
    if "alarm_arn" in value:
        out["AlarmArn"] = value["alarm_arn"]
    if "alarm_configuration_updated_timestamp" in value:
        import capo_cloudwatch.types.timestamp

        out["AlarmConfigurationUpdatedTimestamp"] = (
            capo_cloudwatch.types.timestamp.serialize_aws_json_1_0(
                value["alarm_configuration_updated_timestamp"]
            )
        )
    if "alarm_description" in value:
        out["AlarmDescription"] = value["alarm_description"]
    if "alarm_name" in value:
        out["AlarmName"] = value["alarm_name"]
    if "alarm_rule" in value:
        out["AlarmRule"] = value["alarm_rule"]
    if "insufficient_data_actions" in value:
        import capo_cloudwatch.types.resource_list

        out["InsufficientDataActions"] = (
            capo_cloudwatch.types.resource_list.serialize_aws_json_1_0(
                value["insufficient_data_actions"]
            )
        )
    if "ok_actions" in value:
        import capo_cloudwatch.types.resource_list

        out["OKActions"] = capo_cloudwatch.types.resource_list.serialize_aws_json_1_0(
            value["ok_actions"]
        )
    if "state_reason" in value:
        out["StateReason"] = value["state_reason"]
    if "state_reason_data" in value:
        out["StateReasonData"] = value["state_reason_data"]
    if "state_updated_timestamp" in value:
        import capo_cloudwatch.types.timestamp

        out["StateUpdatedTimestamp"] = (
            capo_cloudwatch.types.timestamp.serialize_aws_json_1_0(
                value["state_updated_timestamp"]
            )
        )
    if "state_value" in value:
        import capo_cloudwatch.types.state_value

        out["StateValue"] = capo_cloudwatch.types.state_value.serialize_aws_json_1_0(
            value["state_value"]
        )
    if "state_transitioned_timestamp" in value:
        import capo_cloudwatch.types.timestamp

        out["StateTransitionedTimestamp"] = (
            capo_cloudwatch.types.timestamp.serialize_aws_json_1_0(
                value["state_transitioned_timestamp"]
            )
        )
    if "actions_suppressed_by" in value:
        import capo_cloudwatch.types.actions_suppressed_by

        out["ActionsSuppressedBy"] = (
            capo_cloudwatch.types.actions_suppressed_by.serialize_aws_json_1_0(
                value["actions_suppressed_by"]
            )
        )
    if "actions_suppressed_reason" in value:
        out["ActionsSuppressedReason"] = value["actions_suppressed_reason"]
    if "actions_suppressor" in value:
        out["ActionsSuppressor"] = value["actions_suppressor"]
    if "actions_suppressor_wait_period" in value:
        out["ActionsSuppressorWaitPeriod"] = value["actions_suppressor_wait_period"]
    if "actions_suppressor_extension_period" in value:
        out["ActionsSuppressorExtensionPeriod"] = value[
            "actions_suppressor_extension_period"
        ]
    return out


def deserialize_aws_json_1_0(data: dict) -> CompositeAlarm:
    out: CompositeAlarm = {}  # type: ignore[typeddict-item]
    if "ActionsEnabled" in data:
        out["actions_enabled"] = data["ActionsEnabled"]
    if "AlarmActions" in data:
        import capo_cloudwatch.types.resource_list

        out["alarm_actions"] = (
            capo_cloudwatch.types.resource_list.deserialize_aws_json_1_0(
                data["AlarmActions"]
            )
        )
    if "AlarmArn" in data:
        out["alarm_arn"] = data["AlarmArn"]
    if "AlarmConfigurationUpdatedTimestamp" in data:
        import capo_cloudwatch.types.timestamp

        out["alarm_configuration_updated_timestamp"] = (
            capo_cloudwatch.types.timestamp.deserialize_aws_json_1_0(
                data["AlarmConfigurationUpdatedTimestamp"]
            )
        )
    if "AlarmDescription" in data:
        out["alarm_description"] = data["AlarmDescription"]
    if "AlarmName" in data:
        out["alarm_name"] = data["AlarmName"]
    if "AlarmRule" in data:
        out["alarm_rule"] = data["AlarmRule"]
    if "InsufficientDataActions" in data:
        import capo_cloudwatch.types.resource_list

        out["insufficient_data_actions"] = (
            capo_cloudwatch.types.resource_list.deserialize_aws_json_1_0(
                data["InsufficientDataActions"]
            )
        )
    if "OKActions" in data:
        import capo_cloudwatch.types.resource_list

        out["ok_actions"] = (
            capo_cloudwatch.types.resource_list.deserialize_aws_json_1_0(
                data["OKActions"]
            )
        )
    if "StateReason" in data:
        out["state_reason"] = data["StateReason"]
    if "StateReasonData" in data:
        out["state_reason_data"] = data["StateReasonData"]
    if "StateUpdatedTimestamp" in data:
        import capo_cloudwatch.types.timestamp

        out["state_updated_timestamp"] = (
            capo_cloudwatch.types.timestamp.deserialize_aws_json_1_0(
                data["StateUpdatedTimestamp"]
            )
        )
    if "StateValue" in data:
        import capo_cloudwatch.types.state_value

        out["state_value"] = capo_cloudwatch.types.state_value.deserialize_aws_json_1_0(
            data["StateValue"]
        )
    if "StateTransitionedTimestamp" in data:
        import capo_cloudwatch.types.timestamp

        out["state_transitioned_timestamp"] = (
            capo_cloudwatch.types.timestamp.deserialize_aws_json_1_0(
                data["StateTransitionedTimestamp"]
            )
        )
    if "ActionsSuppressedBy" in data:
        import capo_cloudwatch.types.actions_suppressed_by

        out["actions_suppressed_by"] = (
            capo_cloudwatch.types.actions_suppressed_by.deserialize_aws_json_1_0(
                data["ActionsSuppressedBy"]
            )
        )
    if "ActionsSuppressedReason" in data:
        out["actions_suppressed_reason"] = data["ActionsSuppressedReason"]
    if "ActionsSuppressor" in data:
        out["actions_suppressor"] = data["ActionsSuppressor"]
    if "ActionsSuppressorWaitPeriod" in data:
        out["actions_suppressor_wait_period"] = data["ActionsSuppressorWaitPeriod"]
    if "ActionsSuppressorExtensionPeriod" in data:
        out["actions_suppressor_extension_period"] = data[
            "ActionsSuppressorExtensionPeriod"
        ]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: CompositeAlarm, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "actions_enabled" in value:
        pairs.append(
            (
                f"{prefix}.ActionsEnabled",
                "true" if value["actions_enabled"] else "false",
            )
        )
    if "alarm_actions" in value:
        import capo_cloudwatch.types.resource_list

        capo_cloudwatch.types.resource_list.serialize_query(
            value["alarm_actions"], pairs, f"{prefix}.AlarmActions"
        )
    if "alarm_arn" in value:
        pairs.append((f"{prefix}.AlarmArn", str(value["alarm_arn"])))
    if "alarm_configuration_updated_timestamp" in value:
        import capo_cloudwatch.types.timestamp

        capo_cloudwatch.types.timestamp.serialize_query(
            value["alarm_configuration_updated_timestamp"],
            pairs,
            f"{prefix}.AlarmConfigurationUpdatedTimestamp",
        )
    if "alarm_description" in value:
        pairs.append((f"{prefix}.AlarmDescription", str(value["alarm_description"])))
    if "alarm_name" in value:
        pairs.append((f"{prefix}.AlarmName", str(value["alarm_name"])))
    if "alarm_rule" in value:
        pairs.append((f"{prefix}.AlarmRule", str(value["alarm_rule"])))
    if "insufficient_data_actions" in value:
        import capo_cloudwatch.types.resource_list

        capo_cloudwatch.types.resource_list.serialize_query(
            value["insufficient_data_actions"],
            pairs,
            f"{prefix}.InsufficientDataActions",
        )
    if "ok_actions" in value:
        import capo_cloudwatch.types.resource_list

        capo_cloudwatch.types.resource_list.serialize_query(
            value["ok_actions"], pairs, f"{prefix}.OKActions"
        )
    if "state_reason" in value:
        pairs.append((f"{prefix}.StateReason", str(value["state_reason"])))
    if "state_reason_data" in value:
        pairs.append((f"{prefix}.StateReasonData", str(value["state_reason_data"])))
    if "state_updated_timestamp" in value:
        import capo_cloudwatch.types.timestamp

        capo_cloudwatch.types.timestamp.serialize_query(
            value["state_updated_timestamp"], pairs, f"{prefix}.StateUpdatedTimestamp"
        )
    if "state_value" in value:
        import capo_cloudwatch.types.state_value

        capo_cloudwatch.types.state_value.serialize_query(
            value["state_value"], pairs, f"{prefix}.StateValue"
        )
    if "state_transitioned_timestamp" in value:
        import capo_cloudwatch.types.timestamp

        capo_cloudwatch.types.timestamp.serialize_query(
            value["state_transitioned_timestamp"],
            pairs,
            f"{prefix}.StateTransitionedTimestamp",
        )
    if "actions_suppressed_by" in value:
        import capo_cloudwatch.types.actions_suppressed_by

        capo_cloudwatch.types.actions_suppressed_by.serialize_query(
            value["actions_suppressed_by"], pairs, f"{prefix}.ActionsSuppressedBy"
        )
    if "actions_suppressed_reason" in value:
        pairs.append(
            (
                f"{prefix}.ActionsSuppressedReason",
                str(value["actions_suppressed_reason"]),
            )
        )
    if "actions_suppressor" in value:
        pairs.append((f"{prefix}.ActionsSuppressor", str(value["actions_suppressor"])))
    if "actions_suppressor_wait_period" in value:
        pairs.append(
            (
                f"{prefix}.ActionsSuppressorWaitPeriod",
                str(value["actions_suppressor_wait_period"]),
            )
        )
    if "actions_suppressor_extension_period" in value:
        pairs.append(
            (
                f"{prefix}.ActionsSuppressorExtensionPeriod",
                str(value["actions_suppressor_extension_period"]),
            )
        )


def deserialize_query(el: Element) -> CompositeAlarm:
    out: CompositeAlarm = {}  # type: ignore[typeddict-item]
    child_actions_enabled = el.find("ActionsEnabled")
    if child_actions_enabled is not None:
        out["actions_enabled"] = (child_actions_enabled.text or "").lower() == "true"
    child_alarm_actions = el.find("AlarmActions")
    if child_alarm_actions is not None:
        import capo_cloudwatch.types.resource_list

        out["alarm_actions"] = capo_cloudwatch.types.resource_list.deserialize_query(
            child_alarm_actions
        )
    child_alarm_arn = el.find("AlarmArn")
    if child_alarm_arn is not None:
        out["alarm_arn"] = str(child_alarm_arn.text or "")
    child_alarm_configuration_updated_timestamp = el.find(
        "AlarmConfigurationUpdatedTimestamp"
    )
    if child_alarm_configuration_updated_timestamp is not None:
        import capo_cloudwatch.types.timestamp

        out["alarm_configuration_updated_timestamp"] = (
            capo_cloudwatch.types.timestamp.deserialize_query(
                child_alarm_configuration_updated_timestamp
            )
        )
    child_alarm_description = el.find("AlarmDescription")
    if child_alarm_description is not None:
        out["alarm_description"] = str(child_alarm_description.text or "")
    child_alarm_name = el.find("AlarmName")
    if child_alarm_name is not None:
        out["alarm_name"] = str(child_alarm_name.text or "")
    child_alarm_rule = el.find("AlarmRule")
    if child_alarm_rule is not None:
        out["alarm_rule"] = str(child_alarm_rule.text or "")
    child_insufficient_data_actions = el.find("InsufficientDataActions")
    if child_insufficient_data_actions is not None:
        import capo_cloudwatch.types.resource_list

        out["insufficient_data_actions"] = (
            capo_cloudwatch.types.resource_list.deserialize_query(
                child_insufficient_data_actions
            )
        )
    child_ok_actions = el.find("OKActions")
    if child_ok_actions is not None:
        import capo_cloudwatch.types.resource_list

        out["ok_actions"] = capo_cloudwatch.types.resource_list.deserialize_query(
            child_ok_actions
        )
    child_state_reason = el.find("StateReason")
    if child_state_reason is not None:
        out["state_reason"] = str(child_state_reason.text or "")
    child_state_reason_data = el.find("StateReasonData")
    if child_state_reason_data is not None:
        out["state_reason_data"] = str(child_state_reason_data.text or "")
    child_state_updated_timestamp = el.find("StateUpdatedTimestamp")
    if child_state_updated_timestamp is not None:
        import capo_cloudwatch.types.timestamp

        out["state_updated_timestamp"] = (
            capo_cloudwatch.types.timestamp.deserialize_query(
                child_state_updated_timestamp
            )
        )
    child_state_value = el.find("StateValue")
    if child_state_value is not None:
        import capo_cloudwatch.types.state_value

        out["state_value"] = capo_cloudwatch.types.state_value.deserialize_query(
            child_state_value
        )
    child_state_transitioned_timestamp = el.find("StateTransitionedTimestamp")
    if child_state_transitioned_timestamp is not None:
        import capo_cloudwatch.types.timestamp

        out["state_transitioned_timestamp"] = (
            capo_cloudwatch.types.timestamp.deserialize_query(
                child_state_transitioned_timestamp
            )
        )
    child_actions_suppressed_by = el.find("ActionsSuppressedBy")
    if child_actions_suppressed_by is not None:
        import capo_cloudwatch.types.actions_suppressed_by

        out["actions_suppressed_by"] = (
            capo_cloudwatch.types.actions_suppressed_by.deserialize_query(
                child_actions_suppressed_by
            )
        )
    child_actions_suppressed_reason = el.find("ActionsSuppressedReason")
    if child_actions_suppressed_reason is not None:
        out["actions_suppressed_reason"] = str(
            child_actions_suppressed_reason.text or ""
        )
    child_actions_suppressor = el.find("ActionsSuppressor")
    if child_actions_suppressor is not None:
        out["actions_suppressor"] = str(child_actions_suppressor.text or "")
    child_actions_suppressor_wait_period = el.find("ActionsSuppressorWaitPeriod")
    if child_actions_suppressor_wait_period is not None:
        out["actions_suppressor_wait_period"] = int(
            child_actions_suppressor_wait_period.text or ""
        )
    child_actions_suppressor_extension_period = el.find(
        "ActionsSuppressorExtensionPeriod"
    )
    if child_actions_suppressor_extension_period is not None:
        out["actions_suppressor_extension_period"] = int(
            child_actions_suppressor_extension_period.text or ""
        )
    return out
