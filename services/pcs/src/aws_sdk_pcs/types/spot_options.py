"""Generated from Smithy shape ``com.amazonaws.pcs#SpotOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pcs.types.spot_allocation_strategy


class SpotOptions(TypedDict):
    allocation_strategy: NotRequired[
        "aws_sdk_pcs.types.spot_allocation_strategy.SpotAllocationStrategy"
    ]
    """<p>The Amazon EC2 allocation strategy PCS uses to provision EC2 instances. PCS supports <b>lowest price</b>, <b>capacity optimized</b>, and <b>price capacity optimized</b>. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet-allocation-strategy.html\">Use allocation strategies to determine how EC2 Fleet or Spot Fleet fulfills Spot and On-Demand capacity</a> in the <i>Amazon Elastic Compute Cloud User Guide</i>. If you don't provide this option, it defaults to <b>price capacity optimized</b>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SpotOptions) -> dict:
    out: dict = {}
    if "allocation_strategy" in value:
        import aws_sdk_pcs.types.spot_allocation_strategy

        out["allocationStrategy"] = (
            aws_sdk_pcs.types.spot_allocation_strategy.serialize_aws_json_1_0(
                value["allocation_strategy"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SpotOptions:
    out: SpotOptions = {}  # type: ignore[typeddict-item]
    if "allocationStrategy" in data:
        import aws_sdk_pcs.types.spot_allocation_strategy

        out["allocation_strategy"] = (
            aws_sdk_pcs.types.spot_allocation_strategy.deserialize_aws_json_1_0(
                data["allocationStrategy"]
            )
        )
    return out
