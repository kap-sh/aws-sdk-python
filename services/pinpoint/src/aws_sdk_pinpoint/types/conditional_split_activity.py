"""Generated from Smithy shape ``com.amazonaws.pinpoint#ConditionalSplitActivity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.condition
    import aws_sdk_pinpoint.types.wait_time


class ConditionalSplitActivity(TypedDict, closed=True):
    condition: NotRequired["aws_sdk_pinpoint.types.condition.Condition"]
    """<p>The conditions that define the paths for the activity, and the relationship between the conditions.</p>"""
    evaluation_wait_time: NotRequired["aws_sdk_pinpoint.types.wait_time.WaitTime"]
    """<p>The amount of time to wait before determining whether the conditions are met, or the date and time when Amazon Pinpoint determines whether the conditions are met.</p>"""
    false_activity: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the activity to perform if the conditions aren't met.</p>"""
    true_activity: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the activity to perform if the conditions are met.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConditionalSplitActivity) -> dict:
    out: dict = {}
    if "condition" in value:
        import aws_sdk_pinpoint.types.condition

        out["Condition"] = aws_sdk_pinpoint.types.condition.serialize_json(
            value["condition"]
        )
    if "evaluation_wait_time" in value:
        import aws_sdk_pinpoint.types.wait_time

        out["EvaluationWaitTime"] = aws_sdk_pinpoint.types.wait_time.serialize_json(
            value["evaluation_wait_time"]
        )
    if "false_activity" in value:
        out["FalseActivity"] = value["false_activity"]
    if "true_activity" in value:
        out["TrueActivity"] = value["true_activity"]
    return out


def deserialize_json(data: dict) -> ConditionalSplitActivity:
    out: ConditionalSplitActivity = {}  # type: ignore[typeddict-item]
    if "Condition" in data:
        import aws_sdk_pinpoint.types.condition

        out["condition"] = aws_sdk_pinpoint.types.condition.deserialize_json(
            data["Condition"]
        )
    if "EvaluationWaitTime" in data:
        import aws_sdk_pinpoint.types.wait_time

        out["evaluation_wait_time"] = aws_sdk_pinpoint.types.wait_time.deserialize_json(
            data["EvaluationWaitTime"]
        )
    if "FalseActivity" in data:
        out["false_activity"] = data["FalseActivity"]
    if "TrueActivity" in data:
        out["true_activity"] = data["TrueActivity"]
    return out
