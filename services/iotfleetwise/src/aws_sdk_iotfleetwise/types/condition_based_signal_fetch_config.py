"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#ConditionBasedSignalFetchConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.fetch_config_event_expression
    import aws_sdk_iotfleetwise.types.trigger_mode


class ConditionBasedSignalFetchConfig(TypedDict, closed=True):
    condition_expression: "aws_sdk_iotfleetwise.types.fetch_config_event_expression.fetchConfigEventExpression"
    """<p>The condition that must be satisfied to trigger a signal fetch.</p>"""
    trigger_mode: "aws_sdk_iotfleetwise.types.trigger_mode.TriggerMode"
    """<p>Indicates the mode in which the signal fetch is triggered.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConditionBasedSignalFetchConfig) -> dict:
    out: dict = {}
    out["conditionExpression"] = value["condition_expression"]
    import aws_sdk_iotfleetwise.types.trigger_mode

    out["triggerMode"] = aws_sdk_iotfleetwise.types.trigger_mode.serialize_aws_json_1_0(
        value["trigger_mode"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ConditionBasedSignalFetchConfig:
    out: ConditionBasedSignalFetchConfig = {}  # type: ignore[typeddict-item]
    if "conditionExpression" in data:
        out["condition_expression"] = data["conditionExpression"]
    else:
        raise DeserializationError(
            "ConditionBasedSignalFetchConfig.condition_expression required"
        )
    if "triggerMode" in data:
        import aws_sdk_iotfleetwise.types.trigger_mode

        out["trigger_mode"] = (
            aws_sdk_iotfleetwise.types.trigger_mode.deserialize_aws_json_1_0(
                data["triggerMode"]
            )
        )
    else:
        raise DeserializationError(
            "ConditionBasedSignalFetchConfig.trigger_mode required"
        )
    return out
