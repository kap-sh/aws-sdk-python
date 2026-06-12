"""Generated from Smithy shape ``com.amazonaws.sagemaker#ThroughputConfigUpdate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.capacity_unit
    import aws_sdk_sagemaker.types.throughput_mode


class ThroughputConfigUpdate(TypedDict):
    throughput_mode: NotRequired[
        "aws_sdk_sagemaker.types.throughput_mode.ThroughputMode"
    ]
    """<p>Target throughput mode of the feature group. Throughput update is an asynchronous operation, and the outcome should be monitored by polling <code>LastUpdateStatus</code> field in <code>DescribeFeatureGroup</code> response. You cannot update a feature group's throughput while another update is in progress. </p>"""
    provisioned_read_capacity_units: NotRequired[
        "aws_sdk_sagemaker.types.capacity_unit.CapacityUnit"
    ]
    """<p>For provisioned feature groups with online store enabled, this indicates the read throughput you are billed for and can consume without throttling. </p>"""
    provisioned_write_capacity_units: NotRequired[
        "aws_sdk_sagemaker.types.capacity_unit.CapacityUnit"
    ]
    """<p>For provisioned feature groups, this indicates the write throughput you are billed for and can consume without throttling. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ThroughputConfigUpdate) -> dict:
    out: dict = {}
    if "throughput_mode" in value:
        import aws_sdk_sagemaker.types.throughput_mode

        out["ThroughputMode"] = (
            aws_sdk_sagemaker.types.throughput_mode.serialize_aws_json_1_1(
                value["throughput_mode"]
            )
        )
    if "provisioned_read_capacity_units" in value:
        out["ProvisionedReadCapacityUnits"] = value["provisioned_read_capacity_units"]
    if "provisioned_write_capacity_units" in value:
        out["ProvisionedWriteCapacityUnits"] = value["provisioned_write_capacity_units"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ThroughputConfigUpdate:
    out: ThroughputConfigUpdate = {}  # type: ignore[typeddict-item]
    if "ThroughputMode" in data:
        import aws_sdk_sagemaker.types.throughput_mode

        out["throughput_mode"] = (
            aws_sdk_sagemaker.types.throughput_mode.deserialize_aws_json_1_1(
                data["ThroughputMode"]
            )
        )
    if "ProvisionedReadCapacityUnits" in data:
        out["provisioned_read_capacity_units"] = data["ProvisionedReadCapacityUnits"]
    if "ProvisionedWriteCapacityUnits" in data:
        out["provisioned_write_capacity_units"] = data["ProvisionedWriteCapacityUnits"]
    return out
