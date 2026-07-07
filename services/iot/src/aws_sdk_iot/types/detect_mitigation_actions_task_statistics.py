"""Generated from Smithy shape ``com.amazonaws.iot#DetectMitigationActionsTaskStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.generic_long_value


class DetectMitigationActionsTaskStatistics(TypedDict, closed=True):
    actions_executed: NotRequired[
        "aws_sdk_iot.types.generic_long_value.GenericLongValue"
    ]
    """<p> The actions that were performed. </p>"""
    actions_skipped: NotRequired[
        "aws_sdk_iot.types.generic_long_value.GenericLongValue"
    ]
    """<p> The actions that were skipped. </p>"""
    actions_failed: NotRequired["aws_sdk_iot.types.generic_long_value.GenericLongValue"]
    """<p> The actions that failed. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DetectMitigationActionsTaskStatistics) -> dict:
    out: dict = {}
    if "actions_executed" in value:
        out["actionsExecuted"] = value["actions_executed"]
    if "actions_skipped" in value:
        out["actionsSkipped"] = value["actions_skipped"]
    if "actions_failed" in value:
        out["actionsFailed"] = value["actions_failed"]
    return out


def deserialize_json(data: dict) -> DetectMitigationActionsTaskStatistics:
    out: DetectMitigationActionsTaskStatistics = {}  # type: ignore[typeddict-item]
    if "actionsExecuted" in data:
        out["actions_executed"] = data["actionsExecuted"]
    if "actionsSkipped" in data:
        out["actions_skipped"] = data["actionsSkipped"]
    if "actionsFailed" in data:
        out["actions_failed"] = data["actionsFailed"]
    return out
