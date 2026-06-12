"""Generated from Smithy shape ``com.amazonaws.timestreamquery#QueryComputeRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_timestream_query.types.compute_mode
    import aws_sdk_timestream_query.types.provisioned_capacity_request


class QueryComputeRequest(TypedDict):
    compute_mode: NotRequired["aws_sdk_timestream_query.types.compute_mode.ComputeMode"]
    """<p>The mode in which Timestream Compute Units (TCUs) are allocated and utilized within an account. Note that in the Asia Pacific (Mumbai) region, the API operation only recognizes the value <code>PROVISIONED</code>.</p>"""
    provisioned_capacity: NotRequired[
        "aws_sdk_timestream_query.types.provisioned_capacity_request.ProvisionedCapacityRequest"
    ]
    """<p>Configuration object that contains settings for provisioned Timestream Compute Units (TCUs) in your account.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: QueryComputeRequest) -> dict:
    out: dict = {}
    if "compute_mode" in value:
        import aws_sdk_timestream_query.types.compute_mode

        out["ComputeMode"] = (
            aws_sdk_timestream_query.types.compute_mode.serialize_aws_json_1_0(
                value["compute_mode"]
            )
        )
    if "provisioned_capacity" in value:
        import aws_sdk_timestream_query.types.provisioned_capacity_request

        out["ProvisionedCapacity"] = (
            aws_sdk_timestream_query.types.provisioned_capacity_request.serialize_aws_json_1_0(
                value["provisioned_capacity"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> QueryComputeRequest:
    out: QueryComputeRequest = {}  # type: ignore[typeddict-item]
    if "ComputeMode" in data:
        import aws_sdk_timestream_query.types.compute_mode

        out["compute_mode"] = (
            aws_sdk_timestream_query.types.compute_mode.deserialize_aws_json_1_0(
                data["ComputeMode"]
            )
        )
    if "ProvisionedCapacity" in data:
        import aws_sdk_timestream_query.types.provisioned_capacity_request

        out["provisioned_capacity"] = (
            aws_sdk_timestream_query.types.provisioned_capacity_request.deserialize_aws_json_1_0(
                data["ProvisionedCapacity"]
            )
        )
    return out
