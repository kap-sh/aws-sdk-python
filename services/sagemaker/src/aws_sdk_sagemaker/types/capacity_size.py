"""Generated from Smithy shape ``com.amazonaws.sagemaker#CapacitySize``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.capacity_size_type
    import aws_sdk_sagemaker.types.capacity_size_value


class CapacitySize(TypedDict, closed=True):
    type: NotRequired["aws_sdk_sagemaker.types.capacity_size_type.CapacitySizeType"]
    """<p>Specifies the endpoint capacity type.</p> <ul> <li> <p> <code>INSTANCE_COUNT</code>: The endpoint activates based on the number of instances.</p> </li> <li> <p> <code>CAPACITY_PERCENT</code>: The endpoint activates based on the specified percentage of capacity.</p> </li> </ul>"""
    value: NotRequired["aws_sdk_sagemaker.types.capacity_size_value.CapacitySizeValue"]
    """<p>Defines the capacity size, either as a number of instances or a capacity percentage.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CapacitySize) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_sagemaker.types.capacity_size_type

        out["Type"] = aws_sdk_sagemaker.types.capacity_size_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CapacitySize:
    out: CapacitySize = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_sagemaker.types.capacity_size_type

        out["type"] = (
            aws_sdk_sagemaker.types.capacity_size_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "Value" in data:
        out["value"] = data["Value"]
    return out
