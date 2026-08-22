"""Generated from Smithy shape ``com.amazonaws.bedrock#ProvisionedModelSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.provisioned_model_summary

ProvisionedModelSummaries: TypeAlias = list[
    "capo_bedrock.types.provisioned_model_summary.ProvisionedModelSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProvisionedModelSummaries) -> list:
    import capo_bedrock.types.provisioned_model_summary

    out: list = []
    for item in value:
        out.append(capo_bedrock.types.provisioned_model_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ProvisionedModelSummaries:
    import capo_bedrock.types.provisioned_model_summary

    out: ProvisionedModelSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock.types.provisioned_model_summary.deserialize_json(item))
    return out
