"""Generated from Smithy shape ``com.amazonaws.quicksight#AnonymousUserDashboardEmbeddingConfigurationEnabledFeature``."""

from typing import Literal, TypeAlias, cast

AnonymousUserDashboardEmbeddingConfigurationEnabledFeature: TypeAlias = Literal[
    "SHARED_VIEW",
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AnonymousUserDashboardEmbeddingConfigurationEnabledFeature,
) -> str:
    return value


def deserialize_json(
    data: str,
) -> AnonymousUserDashboardEmbeddingConfigurationEnabledFeature:
    return cast(AnonymousUserDashboardEmbeddingConfigurationEnabledFeature, data)
