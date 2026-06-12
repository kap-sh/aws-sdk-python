"""Generated from Smithy shape ``com.amazonaws.emr#SpotResizingSpecification``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.spot_provisioning_allocation_strategy
    import aws_sdk_emr.types.whole_number


class SpotResizingSpecification(TypedDict):
    timeout_duration_minutes: NotRequired["aws_sdk_emr.types.whole_number.WholeNumber"]
    """<p>Spot resize timeout in minutes. If Spot Instances are not provisioned within this time, the resize workflow will stop provisioning of Spot instances. Minimum value is 5 minutes and maximum value is 10,080 minutes (7 days). The timeout applies to all resize workflows on the Instance Fleet. The resize could be triggered by Amazon EMR Managed Scaling or by the customer (via Amazon EMR Console, Amazon EMR CLI modify-instance-fleet or Amazon EMR SDK ModifyInstanceFleet API) or by Amazon EMR due to Amazon EC2 Spot Reclamation.</p>"""
    allocation_strategy: NotRequired[
        "aws_sdk_emr.types.spot_provisioning_allocation_strategy.SpotProvisioningAllocationStrategy"
    ]
    """<p>Specifies the allocation strategy to use to launch Spot instances during a resize. If you run Amazon EMR releases 6.9.0 or higher, the default is <code>price-capacity-optimized</code>. If you run Amazon EMR releases 6.8.0 or lower, the default is <code>capacity-optimized</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SpotResizingSpecification) -> dict:
    out: dict = {}
    if "timeout_duration_minutes" in value:
        out["TimeoutDurationMinutes"] = value["timeout_duration_minutes"]
    if "allocation_strategy" in value:
        import aws_sdk_emr.types.spot_provisioning_allocation_strategy

        out["AllocationStrategy"] = (
            aws_sdk_emr.types.spot_provisioning_allocation_strategy.serialize_aws_json_1_1(
                value["allocation_strategy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SpotResizingSpecification:
    out: SpotResizingSpecification = {}  # type: ignore[typeddict-item]
    if "TimeoutDurationMinutes" in data:
        out["timeout_duration_minutes"] = data["TimeoutDurationMinutes"]
    if "AllocationStrategy" in data:
        import aws_sdk_emr.types.spot_provisioning_allocation_strategy

        out["allocation_strategy"] = (
            aws_sdk_emr.types.spot_provisioning_allocation_strategy.deserialize_aws_json_1_1(
                data["AllocationStrategy"]
            )
        )
    return out
