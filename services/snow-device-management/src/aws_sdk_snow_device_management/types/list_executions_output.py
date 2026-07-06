"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#ListExecutionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_snow_device_management.types.execution_summary_list
    import aws_sdk_snow_device_management.types.next_token


class ListExecutionsOutput(TypedDict, closed=True):
    executions: NotRequired[
        "aws_sdk_snow_device_management.types.execution_summary_list.ExecutionSummaryList"
    ]
    """<p>A list of executions. Each execution contains the task ID, the device that the task is executing on, the execution ID, and the status of the execution.</p>"""
    next_token: NotRequired["aws_sdk_snow_device_management.types.next_token.NextToken"]
    """<p>A pagination token to continue to the next page of executions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListExecutionsOutput) -> dict:
    out: dict = {}
    if "executions" in value:
        import aws_sdk_snow_device_management.types.execution_summary_list

        out["executions"] = (
            aws_sdk_snow_device_management.types.execution_summary_list.serialize_json(
                value["executions"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListExecutionsOutput:
    out: ListExecutionsOutput = {}  # type: ignore[typeddict-item]
    if "executions" in data:
        import aws_sdk_snow_device_management.types.execution_summary_list

        out["executions"] = (
            aws_sdk_snow_device_management.types.execution_summary_list.deserialize_json(
                data["executions"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
