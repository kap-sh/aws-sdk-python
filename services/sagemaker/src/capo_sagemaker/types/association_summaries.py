"""Generated from Smithy shape ``com.amazonaws.sagemaker#AssociationSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.association_summary

AssociationSummaries: TypeAlias = list[
    "capo_sagemaker.types.association_summary.AssociationSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociationSummaries) -> list:
    import capo_sagemaker.types.association_summary

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.association_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AssociationSummaries:
    import capo_sagemaker.types.association_summary

    out: AssociationSummaries = []
    for item in data:
        out.append(
            capo_sagemaker.types.association_summary.deserialize_aws_json_1_1(item)
        )
    return out
