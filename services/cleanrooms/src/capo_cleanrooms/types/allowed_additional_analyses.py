"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AllowedAdditionalAnalyses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.additional_analyses_resource_arn

AllowedAdditionalAnalyses: TypeAlias = list[
    "capo_cleanrooms.types.additional_analyses_resource_arn.AdditionalAnalysesResourceArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: AllowedAdditionalAnalyses) -> list:
    return list(value)


def deserialize_json(data: list) -> AllowedAdditionalAnalyses:
    return list(data)
