"""Generated from Smithy shape ``com.amazonaws.batch#DescribeComputeEnvironmentsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.compute_environment_detail_list
    import aws_sdk_batch.types.string


class DescribeComputeEnvironmentsResponse(TypedDict):
    compute_environments: NotRequired[
        "aws_sdk_batch.types.compute_environment_detail_list.ComputeEnvironmentDetailList"
    ]
    """<p>The list of compute environments.</p>"""
    next_token: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The <code>nextToken</code> value to include in a future <code>DescribeComputeEnvironments</code> request. When the results of a <code>DescribeComputeEnvironments</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeComputeEnvironmentsResponse) -> dict:
    out: dict = {}
    if "compute_environments" in value:
        import aws_sdk_batch.types.compute_environment_detail_list

        out["computeEnvironments"] = (
            aws_sdk_batch.types.compute_environment_detail_list.serialize_json(
                value["compute_environments"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeComputeEnvironmentsResponse:
    out: DescribeComputeEnvironmentsResponse = {}  # type: ignore[typeddict-item]
    if "computeEnvironments" in data:
        import aws_sdk_batch.types.compute_environment_detail_list

        out["compute_environments"] = (
            aws_sdk_batch.types.compute_environment_detail_list.deserialize_json(
                data["computeEnvironments"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
