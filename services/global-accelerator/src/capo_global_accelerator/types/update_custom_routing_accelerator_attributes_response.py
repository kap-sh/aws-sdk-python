"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#UpdateCustomRoutingAcceleratorAttributesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_global_accelerator.types.custom_routing_accelerator_attributes


class UpdateCustomRoutingAcceleratorAttributesResponse(TypedDict, closed=True):
    accelerator_attributes: NotRequired[
        "capo_global_accelerator.types.custom_routing_accelerator_attributes.CustomRoutingAcceleratorAttributes"
    ]
    """<p>Updated custom routing accelerator.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: UpdateCustomRoutingAcceleratorAttributesResponse,
) -> dict:
    out: dict = {}
    if "accelerator_attributes" in value:
        import capo_global_accelerator.types.custom_routing_accelerator_attributes

        out["AcceleratorAttributes"] = (
            capo_global_accelerator.types.custom_routing_accelerator_attributes.serialize_aws_json_1_1(
                value["accelerator_attributes"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> UpdateCustomRoutingAcceleratorAttributesResponse:
    out: UpdateCustomRoutingAcceleratorAttributesResponse = {}  # type: ignore[typeddict-item]
    if "AcceleratorAttributes" in data:
        import capo_global_accelerator.types.custom_routing_accelerator_attributes

        out["accelerator_attributes"] = (
            capo_global_accelerator.types.custom_routing_accelerator_attributes.deserialize_aws_json_1_1(
                data["AcceleratorAttributes"]
            )
        )
    return out
