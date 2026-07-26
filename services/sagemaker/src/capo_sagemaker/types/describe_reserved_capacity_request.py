"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeReservedCapacityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.reserved_capacity_arn


class DescribeReservedCapacityRequest(TypedDict, closed=True):
    reserved_capacity_arn: NotRequired[
        "capo_sagemaker.types.reserved_capacity_arn.ReservedCapacityArn"
    ]
    """<p>ARN of the reserved capacity to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeReservedCapacityRequest) -> dict:
    out: dict = {}
    if "reserved_capacity_arn" in value:
        out["ReservedCapacityArn"] = value["reserved_capacity_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeReservedCapacityRequest:
    out: DescribeReservedCapacityRequest = {}  # type: ignore[typeddict-item]
    if "ReservedCapacityArn" in data:
        out["reserved_capacity_arn"] = data["ReservedCapacityArn"]
    return out
