"""Generated from Smithy shape ``com.amazonaws.sagemaker#PlacementSpecifications``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.placement_specification

PlacementSpecifications: TypeAlias = list[
    "aws_sdk_sagemaker.types.placement_specification.PlacementSpecification"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlacementSpecifications) -> list:
    import aws_sdk_sagemaker.types.placement_specification

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.placement_specification.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PlacementSpecifications:
    import aws_sdk_sagemaker.types.placement_specification

    out: PlacementSpecifications = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.placement_specification.deserialize_aws_json_1_1(
                item
            )
        )
    return out
