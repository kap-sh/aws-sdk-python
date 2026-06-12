"""Generated from Smithy shape ``com.amazonaws.sagemaker#ThroughputConfigDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.capacity_unit
    import aws_sdk_sagemaker.types.throughput_mode


class ThroughputConfigDescription(TypedDict):
    throughput_mode: NotRequired[
        "aws_sdk_sagemaker.types.throughput_mode.ThroughputMode"
    ]
    """<p>The mode used for your feature group throughput: <code>ON_DEMAND</code> or <code>PROVISIONED</code>. </p>"""
    provisioned_read_capacity_units: NotRequired[
        "aws_sdk_sagemaker.types.capacity_unit.CapacityUnit"
    ]
    """<p> For provisioned feature groups with online store enabled, this indicates the read throughput you are billed for and can consume without throttling. </p> <p>This field is not applicable for on-demand feature groups. </p>"""
    provisioned_write_capacity_units: NotRequired[
        "aws_sdk_sagemaker.types.capacity_unit.CapacityUnit"
    ]
    """<p> For provisioned feature groups, this indicates the write throughput you are billed for and can consume without throttling. </p> <p>This field is not applicable for on-demand feature groups. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ThroughputConfigDescription) -> dict:
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


def deserialize_aws_json_1_1(data: dict) -> ThroughputConfigDescription:
    out: ThroughputConfigDescription = {}  # type: ignore[typeddict-item]
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
