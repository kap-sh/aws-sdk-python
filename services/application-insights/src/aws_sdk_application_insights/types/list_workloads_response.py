"""Generated from Smithy shape ``com.amazonaws.applicationinsights#ListWorkloadsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_application_insights.types.pagination_token
    import aws_sdk_application_insights.types.workload_list


class ListWorkloadsResponse(TypedDict):
    workload_list: NotRequired[
        "aws_sdk_application_insights.types.workload_list.WorkloadList"
    ]
    """<p>The list of workloads.</p>"""
    next_token: NotRequired[
        "aws_sdk_application_insights.types.pagination_token.PaginationToken"
    ]
    """<p>The token to request the next page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListWorkloadsResponse) -> dict:
    out: dict = {}
    if "workload_list" in value:
        import aws_sdk_application_insights.types.workload_list

        out["WorkloadList"] = (
            aws_sdk_application_insights.types.workload_list.serialize_aws_json_1_1(
                value["workload_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListWorkloadsResponse:
    out: ListWorkloadsResponse = {}  # type: ignore[typeddict-item]
    if "WorkloadList" in data:
        import aws_sdk_application_insights.types.workload_list

        out["workload_list"] = (
            aws_sdk_application_insights.types.workload_list.deserialize_aws_json_1_1(
                data["WorkloadList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
