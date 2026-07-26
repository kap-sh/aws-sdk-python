"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#UpdateCustomRoutingAcceleratorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_global_accelerator.types.custom_routing_accelerator


class UpdateCustomRoutingAcceleratorResponse(TypedDict, closed=True):
    accelerator: NotRequired[
        "capo_global_accelerator.types.custom_routing_accelerator.CustomRoutingAccelerator"
    ]
    """<p>Information about the updated custom routing accelerator.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateCustomRoutingAcceleratorResponse) -> dict:
    out: dict = {}
    if "accelerator" in value:
        import capo_global_accelerator.types.custom_routing_accelerator

        out["Accelerator"] = (
            capo_global_accelerator.types.custom_routing_accelerator.serialize_aws_json_1_1(
                value["accelerator"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateCustomRoutingAcceleratorResponse:
    out: UpdateCustomRoutingAcceleratorResponse = {}  # type: ignore[typeddict-item]
    if "Accelerator" in data:
        import capo_global_accelerator.types.custom_routing_accelerator

        out["accelerator"] = (
            capo_global_accelerator.types.custom_routing_accelerator.deserialize_aws_json_1_1(
                data["Accelerator"]
            )
        )
    return out
