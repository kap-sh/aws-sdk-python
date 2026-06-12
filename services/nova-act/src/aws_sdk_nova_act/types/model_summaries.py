"""Generated from Smithy shape ``com.amazonaws.novaact#ModelSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_nova_act.types.model_summary

ModelSummaries: TypeAlias = list["aws_sdk_nova_act.types.model_summary.ModelSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: ModelSummaries) -> list:
    import aws_sdk_nova_act.types.model_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_nova_act.types.model_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ModelSummaries:
    import aws_sdk_nova_act.types.model_summary

    out: ModelSummaries = []
    for item in data:
        out.append(aws_sdk_nova_act.types.model_summary.deserialize_json(item))
    return out
