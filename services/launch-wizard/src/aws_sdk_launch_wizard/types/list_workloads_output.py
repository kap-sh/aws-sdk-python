"""Generated from Smithy shape ``com.amazonaws.launchwizard#ListWorkloadsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_launch_wizard.types.next_token
    import aws_sdk_launch_wizard.types.workload_data_summary_list


class ListWorkloadsOutput(TypedDict):
    workloads: NotRequired[
        "aws_sdk_launch_wizard.types.workload_data_summary_list.WorkloadDataSummaryList"
    ]
    """<p>Information about the workloads.</p>"""
    next_token: NotRequired["aws_sdk_launch_wizard.types.next_token.NextToken"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkloadsOutput) -> dict:
    out: dict = {}
    if "workloads" in value:
        import aws_sdk_launch_wizard.types.workload_data_summary_list

        out["workloads"] = (
            aws_sdk_launch_wizard.types.workload_data_summary_list.serialize_json(
                value["workloads"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListWorkloadsOutput:
    out: ListWorkloadsOutput = {}  # type: ignore[typeddict-item]
    if "workloads" in data:
        import aws_sdk_launch_wizard.types.workload_data_summary_list

        out["workloads"] = (
            aws_sdk_launch_wizard.types.workload_data_summary_list.deserialize_json(
                data["workloads"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
