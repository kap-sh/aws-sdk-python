"""Generated from Smithy shape ``com.amazonaws.appflow#ExecutionDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.date
    import capo_appflow.types.execution_status
    import capo_appflow.types.most_recent_execution_message


class ExecutionDetails(TypedDict, closed=True):
    most_recent_execution_message: NotRequired[
        "capo_appflow.types.most_recent_execution_message.MostRecentExecutionMessage"
    ]
    """<p> Describes the details of the most recent flow run. </p>"""
    most_recent_execution_time: NotRequired["capo_appflow.types.date.Date"]
    """<p> Specifies the time of the most recent flow run. </p>"""
    most_recent_execution_status: NotRequired[
        "capo_appflow.types.execution_status.ExecutionStatus"
    ]
    """<p> Specifies the status of the most recent flow run. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionDetails) -> dict:
    out: dict = {}
    if "most_recent_execution_message" in value:
        out["mostRecentExecutionMessage"] = value["most_recent_execution_message"]
    if "most_recent_execution_time" in value:
        import capo_appflow.types.date

        out["mostRecentExecutionTime"] = capo_appflow.types.date.serialize_json(
            value["most_recent_execution_time"]
        )
    if "most_recent_execution_status" in value:
        import capo_appflow.types.execution_status

        out["mostRecentExecutionStatus"] = (
            capo_appflow.types.execution_status.serialize_json(
                value["most_recent_execution_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExecutionDetails:
    out: ExecutionDetails = {}  # type: ignore[typeddict-item]
    if "mostRecentExecutionMessage" in data:
        out["most_recent_execution_message"] = data["mostRecentExecutionMessage"]
    if "mostRecentExecutionTime" in data:
        import capo_appflow.types.date

        out["most_recent_execution_time"] = capo_appflow.types.date.deserialize_json(
            data["mostRecentExecutionTime"]
        )
    if "mostRecentExecutionStatus" in data:
        import capo_appflow.types.execution_status

        out["most_recent_execution_status"] = (
            capo_appflow.types.execution_status.deserialize_json(
                data["mostRecentExecutionStatus"]
            )
        )
    return out
