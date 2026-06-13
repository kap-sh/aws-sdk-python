"""Generated from Smithy shape ``com.amazonaws.emr#ListStepsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.marker
    import aws_sdk_emr.types.step_summary_list


class ListStepsOutput(TypedDict):
    steps: NotRequired["aws_sdk_emr.types.step_summary_list.StepSummaryList"]
    """<p>The filtered list of steps for the cluster.</p>"""
    marker: NotRequired["aws_sdk_emr.types.marker.Marker"]
    """<p>The maximum number of steps that a single <code>ListSteps</code> action returns is 50. To return a longer list of steps, use multiple <code>ListSteps</code> actions along with the <code>Marker</code> parameter, which is a pagination token that indicates the next set of results to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListStepsOutput) -> dict:
    out: dict = {}
    if "steps" in value:
        import aws_sdk_emr.types.step_summary_list

        out["Steps"] = aws_sdk_emr.types.step_summary_list.serialize_aws_json_1_1(
            value["steps"]
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListStepsOutput:
    out: ListStepsOutput = {}  # type: ignore[typeddict-item]
    if "Steps" in data:
        import aws_sdk_emr.types.step_summary_list

        out["steps"] = aws_sdk_emr.types.step_summary_list.deserialize_aws_json_1_1(
            data["Steps"]
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
