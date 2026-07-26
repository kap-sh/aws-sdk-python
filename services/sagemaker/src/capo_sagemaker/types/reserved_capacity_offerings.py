"""Generated from Smithy shape ``com.amazonaws.sagemaker#ReservedCapacityOfferings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.reserved_capacity_offering

ReservedCapacityOfferings: TypeAlias = list[
    "capo_sagemaker.types.reserved_capacity_offering.ReservedCapacityOffering"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReservedCapacityOfferings) -> list:
    import capo_sagemaker.types.reserved_capacity_offering

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.reserved_capacity_offering.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ReservedCapacityOfferings:
    import capo_sagemaker.types.reserved_capacity_offering

    out: ReservedCapacityOfferings = []
    for item in data:
        out.append(
            capo_sagemaker.types.reserved_capacity_offering.deserialize_aws_json_1_1(
                item
            )
        )
    return out
