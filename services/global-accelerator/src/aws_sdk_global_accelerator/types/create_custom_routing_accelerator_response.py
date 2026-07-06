"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#CreateCustomRoutingAcceleratorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.custom_routing_accelerator


class CreateCustomRoutingAcceleratorResponse(TypedDict, closed=True):
    accelerator: NotRequired[
        "aws_sdk_global_accelerator.types.custom_routing_accelerator.CustomRoutingAccelerator"
    ]
    """<p>The accelerator that is created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateCustomRoutingAcceleratorResponse) -> dict:
    out: dict = {}
    if "accelerator" in value:
        import aws_sdk_global_accelerator.types.custom_routing_accelerator

        out["Accelerator"] = (
            aws_sdk_global_accelerator.types.custom_routing_accelerator.serialize_aws_json_1_1(
                value["accelerator"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateCustomRoutingAcceleratorResponse:
    out: CreateCustomRoutingAcceleratorResponse = {}  # type: ignore[typeddict-item]
    if "Accelerator" in data:
        import aws_sdk_global_accelerator.types.custom_routing_accelerator

        out["accelerator"] = (
            aws_sdk_global_accelerator.types.custom_routing_accelerator.deserialize_aws_json_1_1(
                data["Accelerator"]
            )
        )
    return out
