"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#DescribeAcceleratorAttributesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.accelerator_attributes


class DescribeAcceleratorAttributesResponse(TypedDict):
    accelerator_attributes: NotRequired[
        "aws_sdk_global_accelerator.types.accelerator_attributes.AcceleratorAttributes"
    ]
    """<p>The attributes of the accelerator.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAcceleratorAttributesResponse) -> dict:
    out: dict = {}
    if "accelerator_attributes" in value:
        import aws_sdk_global_accelerator.types.accelerator_attributes

        out["AcceleratorAttributes"] = (
            aws_sdk_global_accelerator.types.accelerator_attributes.serialize_aws_json_1_1(
                value["accelerator_attributes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAcceleratorAttributesResponse:
    out: DescribeAcceleratorAttributesResponse = {}  # type: ignore[typeddict-item]
    if "AcceleratorAttributes" in data:
        import aws_sdk_global_accelerator.types.accelerator_attributes

        out["accelerator_attributes"] = (
            aws_sdk_global_accelerator.types.accelerator_attributes.deserialize_aws_json_1_1(
                data["AcceleratorAttributes"]
            )
        )
    return out
