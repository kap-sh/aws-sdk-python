"""Generated from Smithy shape ``com.amazonaws.bedrock#ProvisionedModelSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.provisioned_model_summary

ProvisionedModelSummaries: TypeAlias = list[
    "aws_sdk_bedrock.types.provisioned_model_summary.ProvisionedModelSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProvisionedModelSummaries) -> list:
    import aws_sdk_bedrock.types.provisioned_model_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock.types.provisioned_model_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ProvisionedModelSummaries:
    import aws_sdk_bedrock.types.provisioned_model_summary

    out: ProvisionedModelSummaries = []
    for item in data:
        out.append(
            aws_sdk_bedrock.types.provisioned_model_summary.deserialize_json(item)
        )
    return out
