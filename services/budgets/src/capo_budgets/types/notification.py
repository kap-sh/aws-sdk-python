"""Generated from Smithy shape ``com.amazonaws.budgets#Notification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_budgets.errors import DeserializationError

if TYPE_CHECKING:
    import capo_budgets.types.comparison_operator
    import capo_budgets.types.notification_state
    import capo_budgets.types.notification_threshold
    import capo_budgets.types.notification_type
    import capo_budgets.types.threshold_type


class Notification(TypedDict, closed=True):
    notification_type: "capo_budgets.types.notification_type.NotificationType"
    """<p>Specifies whether the notification is for how much you have spent (<code>ACTUAL</code>) or for how much that you're forecasted to spend (<code>FORECASTED</code>).</p>"""
    comparison_operator: "capo_budgets.types.comparison_operator.ComparisonOperator"
    """<p>The comparison that's used for this notification.</p>"""
    threshold: "capo_budgets.types.notification_threshold.NotificationThreshold"
    """<p>The threshold that's associated with a notification. Thresholds are always a percentage, and many customers find value being alerted between 50% - 200% of the budgeted amount. The maximum limit for your threshold is 1,000,000% above the budgeted amount.</p>"""
    threshold_type: NotRequired["capo_budgets.types.threshold_type.ThresholdType"]
    """<p>The type of threshold for a notification. For <code>ABSOLUTE_VALUE</code> thresholds, Amazon Web Services notifies you when you go over or are forecasted to go over your total cost threshold. For <code>PERCENTAGE</code> thresholds, Amazon Web Services notifies you when you go over or are forecasted to go over a certain percentage of your forecasted spend. For example, if you have a budget for 200 dollars and you have a <code>PERCENTAGE</code> threshold of 80%, Amazon Web Services notifies you when you go over 160 dollars.</p>"""
    notification_state: NotRequired[
        "capo_budgets.types.notification_state.NotificationState"
    ]
    """<p>Specifies whether this notification is in alarm. If a budget notification is in the <code>ALARM</code> state, you passed the set threshold for the budget.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Notification) -> dict:
    out: dict = {}
    import capo_budgets.types.notification_type

    out["NotificationType"] = (
        capo_budgets.types.notification_type.serialize_aws_json_1_1(
            value["notification_type"]
        )
    )
    import capo_budgets.types.comparison_operator

    out["ComparisonOperator"] = (
        capo_budgets.types.comparison_operator.serialize_aws_json_1_1(
            value["comparison_operator"]
        )
    )
    out["Threshold"] = value.get("threshold", 0)
    if "threshold_type" in value:
        import capo_budgets.types.threshold_type

        out["ThresholdType"] = capo_budgets.types.threshold_type.serialize_aws_json_1_1(
            value["threshold_type"]
        )
    if "notification_state" in value:
        import capo_budgets.types.notification_state

        out["NotificationState"] = (
            capo_budgets.types.notification_state.serialize_aws_json_1_1(
                value["notification_state"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Notification:
    out: Notification = {}  # type: ignore[typeddict-item]
    if "NotificationType" in data:
        import capo_budgets.types.notification_type

        out["notification_type"] = (
            capo_budgets.types.notification_type.deserialize_aws_json_1_1(
                data["NotificationType"]
            )
        )
    else:
        raise DeserializationError("Notification.notification_type required")
    if "ComparisonOperator" in data:
        import capo_budgets.types.comparison_operator

        out["comparison_operator"] = (
            capo_budgets.types.comparison_operator.deserialize_aws_json_1_1(
                data["ComparisonOperator"]
            )
        )
    else:
        raise DeserializationError("Notification.comparison_operator required")
    if "Threshold" in data:
        out["threshold"] = data["Threshold"]
    else:
        out["threshold"] = 0
    if "ThresholdType" in data:
        import capo_budgets.types.threshold_type

        out["threshold_type"] = (
            capo_budgets.types.threshold_type.deserialize_aws_json_1_1(
                data["ThresholdType"]
            )
        )
    if "NotificationState" in data:
        import capo_budgets.types.notification_state

        out["notification_state"] = (
            capo_budgets.types.notification_state.deserialize_aws_json_1_1(
                data["NotificationState"]
            )
        )
    return out
