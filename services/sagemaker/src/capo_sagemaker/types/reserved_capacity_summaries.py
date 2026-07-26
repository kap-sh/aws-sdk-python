"""Generated from Smithy shape ``com.amazonaws.sagemaker#ReservedCapacitySummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.reserved_capacity_summary

ReservedCapacitySummaries: TypeAlias = list[
    "capo_sagemaker.types.reserved_capacity_summary.ReservedCapacitySummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReservedCapacitySummaries) -> list:
    import capo_sagemaker.types.reserved_capacity_summary

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.reserved_capacity_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ReservedCapacitySummaries:
    import capo_sagemaker.types.reserved_capacity_summary

    out: ReservedCapacitySummaries = []
    for item in data:
        out.append(
            capo_sagemaker.types.reserved_capacity_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
