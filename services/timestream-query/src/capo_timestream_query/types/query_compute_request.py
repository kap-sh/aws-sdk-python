"""Generated from Smithy shape ``com.amazonaws.timestreamquery#QueryComputeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_query.types.compute_mode
    import capo_timestream_query.types.provisioned_capacity_request


class QueryComputeRequest(TypedDict, closed=True):
    compute_mode: NotRequired["capo_timestream_query.types.compute_mode.ComputeMode"]
    """<p>The mode in which Timestream Compute Units (TCUs) are allocated and utilized within an account. Note that in the Asia Pacific (Mumbai) region, the API operation only recognizes the value <code>PROVISIONED</code>.</p>"""
    provisioned_capacity: NotRequired[
        "capo_timestream_query.types.provisioned_capacity_request.ProvisionedCapacityRequest"
    ]
    """<p>Configuration object that contains settings for provisioned Timestream Compute Units (TCUs) in your account.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: QueryComputeRequest) -> dict:
    out: dict = {}
    if "compute_mode" in value:
        import capo_timestream_query.types.compute_mode

        out["ComputeMode"] = (
            capo_timestream_query.types.compute_mode.serialize_aws_json_1_0(
                value["compute_mode"]
            )
        )
    if "provisioned_capacity" in value:
        import capo_timestream_query.types.provisioned_capacity_request

        out["ProvisionedCapacity"] = (
            capo_timestream_query.types.provisioned_capacity_request.serialize_aws_json_1_0(
                value["provisioned_capacity"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> QueryComputeRequest:
    out: QueryComputeRequest = {}  # type: ignore[typeddict-item]
    if "ComputeMode" in data:
        import capo_timestream_query.types.compute_mode

        out["compute_mode"] = (
            capo_timestream_query.types.compute_mode.deserialize_aws_json_1_0(
                data["ComputeMode"]
            )
        )
    if "ProvisionedCapacity" in data:
        import capo_timestream_query.types.provisioned_capacity_request

        out["provisioned_capacity"] = (
            capo_timestream_query.types.provisioned_capacity_request.deserialize_aws_json_1_0(
                data["ProvisionedCapacity"]
            )
        )
    return out
