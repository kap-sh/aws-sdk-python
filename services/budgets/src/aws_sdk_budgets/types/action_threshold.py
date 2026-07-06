"""Generated from Smithy shape ``com.amazonaws.budgets#ActionThreshold``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_budgets.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_budgets.types.notification_threshold
    import aws_sdk_budgets.types.threshold_type


class ActionThreshold(TypedDict, closed=True):
    action_threshold_value: (
        "aws_sdk_budgets.types.notification_threshold.NotificationThreshold"
    )
    action_threshold_type: "aws_sdk_budgets.types.threshold_type.ThresholdType"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionThreshold) -> dict:
    out: dict = {}
    out["ActionThresholdValue"] = value.get("action_threshold_value", 0)
    import aws_sdk_budgets.types.threshold_type

    out["ActionThresholdType"] = (
        aws_sdk_budgets.types.threshold_type.serialize_aws_json_1_1(
            value["action_threshold_type"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ActionThreshold:
    out: ActionThreshold = {}  # type: ignore[typeddict-item]
    if "ActionThresholdValue" in data:
        out["action_threshold_value"] = data["ActionThresholdValue"]
    else:
        out["action_threshold_value"] = 0
    if "ActionThresholdType" in data:
        import aws_sdk_budgets.types.threshold_type

        out["action_threshold_type"] = (
            aws_sdk_budgets.types.threshold_type.deserialize_aws_json_1_1(
                data["ActionThresholdType"]
            )
        )
    else:
        raise DeserializationError("ActionThreshold.action_threshold_type required")
    return out
