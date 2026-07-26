"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#UpdateAcceleratorAttributesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_global_accelerator.types.accelerator_attributes


class UpdateAcceleratorAttributesResponse(TypedDict, closed=True):
    accelerator_attributes: NotRequired[
        "capo_global_accelerator.types.accelerator_attributes.AcceleratorAttributes"
    ]
    """<p>Updated attributes for the accelerator.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateAcceleratorAttributesResponse) -> dict:
    out: dict = {}
    if "accelerator_attributes" in value:
        import capo_global_accelerator.types.accelerator_attributes

        out["AcceleratorAttributes"] = (
            capo_global_accelerator.types.accelerator_attributes.serialize_aws_json_1_1(
                value["accelerator_attributes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateAcceleratorAttributesResponse:
    out: UpdateAcceleratorAttributesResponse = {}  # type: ignore[typeddict-item]
    if "AcceleratorAttributes" in data:
        import capo_global_accelerator.types.accelerator_attributes

        out["accelerator_attributes"] = (
            capo_global_accelerator.types.accelerator_attributes.deserialize_aws_json_1_1(
                data["AcceleratorAttributes"]
            )
        )
    return out
