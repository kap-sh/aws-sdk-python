"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListUltraServersByReservedCapacityRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.max_results
    import aws_sdk_sagemaker.types.next_token
    import aws_sdk_sagemaker.types.reserved_capacity_arn


class ListUltraServersByReservedCapacityRequest(TypedDict):
    reserved_capacity_arn: NotRequired[
        "aws_sdk_sagemaker.types.reserved_capacity_arn.ReservedCapacityArn"
    ]
    """<p>The ARN of the reserved capacity to list UltraServers for.</p>"""
    max_results: NotRequired["aws_sdk_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of UltraServers to return in the response. The default value is 10.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the previous response was truncated, you receive this token. Use it in your next request to receive the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListUltraServersByReservedCapacityRequest) -> dict:
    out: dict = {}
    if "reserved_capacity_arn" in value:
        out["ReservedCapacityArn"] = value["reserved_capacity_arn"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListUltraServersByReservedCapacityRequest:
    out: ListUltraServersByReservedCapacityRequest = {}  # type: ignore[typeddict-item]
    if "ReservedCapacityArn" in data:
        out["reserved_capacity_arn"] = data["ReservedCapacityArn"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
