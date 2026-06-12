"""Generated from Smithy shape ``com.amazonaws.pinpoint#MultiConditionalSplitActivity``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.list_of_multi_conditional_branch
    import aws_sdk_pinpoint.types.wait_time


class MultiConditionalSplitActivity(TypedDict):
    branches: NotRequired[
        "aws_sdk_pinpoint.types.list_of_multi_conditional_branch.ListOfMultiConditionalBranch"
    ]
    """<p>The paths for the activity, including the conditions for entering each path and the activity to perform for each path.</p>"""
    default_activity: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the activity to perform for participants who don't meet any of the conditions specified for other paths in the activity.</p>"""
    evaluation_wait_time: NotRequired["aws_sdk_pinpoint.types.wait_time.WaitTime"]
    """<p>The amount of time to wait or the date and time when Amazon Pinpoint determines whether the conditions are met.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MultiConditionalSplitActivity) -> dict:
    out: dict = {}
    if "branches" in value:
        import aws_sdk_pinpoint.types.list_of_multi_conditional_branch

        out["Branches"] = (
            aws_sdk_pinpoint.types.list_of_multi_conditional_branch.serialize_json(
                value["branches"]
            )
        )
    if "default_activity" in value:
        out["DefaultActivity"] = value["default_activity"]
    if "evaluation_wait_time" in value:
        import aws_sdk_pinpoint.types.wait_time

        out["EvaluationWaitTime"] = aws_sdk_pinpoint.types.wait_time.serialize_json(
            value["evaluation_wait_time"]
        )
    return out


def deserialize_json(data: dict) -> MultiConditionalSplitActivity:
    out: MultiConditionalSplitActivity = {}  # type: ignore[typeddict-item]
    if "Branches" in data:
        import aws_sdk_pinpoint.types.list_of_multi_conditional_branch

        out["branches"] = (
            aws_sdk_pinpoint.types.list_of_multi_conditional_branch.deserialize_json(
                data["Branches"]
            )
        )
    if "DefaultActivity" in data:
        out["default_activity"] = data["DefaultActivity"]
    if "EvaluationWaitTime" in data:
        import aws_sdk_pinpoint.types.wait_time

        out["evaluation_wait_time"] = aws_sdk_pinpoint.types.wait_time.deserialize_json(
            data["EvaluationWaitTime"]
        )
    return out
