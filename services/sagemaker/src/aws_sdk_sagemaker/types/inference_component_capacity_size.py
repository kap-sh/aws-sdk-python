"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceComponentCapacitySize``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.capacity_size_value
    import aws_sdk_sagemaker.types.inference_component_capacity_size_type


class InferenceComponentCapacitySize(TypedDict, closed=True):
    type: NotRequired[
        "aws_sdk_sagemaker.types.inference_component_capacity_size_type.InferenceComponentCapacitySizeType"
    ]
    """<p>Specifies the endpoint capacity type.</p> <dl> <dt>COPY_COUNT</dt> <dd> <p>The endpoint activates based on the number of inference component copies.</p> </dd> <dt>CAPACITY_PERCENT</dt> <dd> <p>The endpoint activates based on the specified percentage of capacity.</p> </dd> </dl>"""
    value: NotRequired["aws_sdk_sagemaker.types.capacity_size_value.CapacitySizeValue"]
    """<p>Defines the capacity size, either as a number of inference component copies or a capacity percentage.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferenceComponentCapacitySize) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_sagemaker.types.inference_component_capacity_size_type

        out["Type"] = (
            aws_sdk_sagemaker.types.inference_component_capacity_size_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InferenceComponentCapacitySize:
    out: InferenceComponentCapacitySize = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_sagemaker.types.inference_component_capacity_size_type

        out["type"] = (
            aws_sdk_sagemaker.types.inference_component_capacity_size_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "Value" in data:
        out["value"] = data["Value"]
    return out
