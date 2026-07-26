"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#DescribeCustomRoutingAcceleratorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_global_accelerator.types.custom_routing_accelerator


class DescribeCustomRoutingAcceleratorResponse(TypedDict, closed=True):
    accelerator: NotRequired[
        "capo_global_accelerator.types.custom_routing_accelerator.CustomRoutingAccelerator"
    ]
    """<p>The description of the custom routing accelerator.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCustomRoutingAcceleratorResponse) -> dict:
    out: dict = {}
    if "accelerator" in value:
        import capo_global_accelerator.types.custom_routing_accelerator

        out["Accelerator"] = (
            capo_global_accelerator.types.custom_routing_accelerator.serialize_aws_json_1_1(
                value["accelerator"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCustomRoutingAcceleratorResponse:
    out: DescribeCustomRoutingAcceleratorResponse = {}  # type: ignore[typeddict-item]
    if "Accelerator" in data:
        import capo_global_accelerator.types.custom_routing_accelerator

        out["accelerator"] = (
            capo_global_accelerator.types.custom_routing_accelerator.deserialize_aws_json_1_1(
                data["Accelerator"]
            )
        )
    return out
