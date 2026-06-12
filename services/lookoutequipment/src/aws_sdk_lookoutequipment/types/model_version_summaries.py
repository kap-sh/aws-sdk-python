"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#ModelVersionSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.model_version_summary

ModelVersionSummaries: TypeAlias = list[
    "aws_sdk_lookoutequipment.types.model_version_summary.ModelVersionSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ModelVersionSummaries) -> list:
    import aws_sdk_lookoutequipment.types.model_version_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lookoutequipment.types.model_version_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ModelVersionSummaries:
    import aws_sdk_lookoutequipment.types.model_version_summary

    out: ModelVersionSummaries = []
    for item in data:
        out.append(
            aws_sdk_lookoutequipment.types.model_version_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
