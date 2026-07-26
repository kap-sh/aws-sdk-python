"""Generated from Smithy shape ``com.amazonaws.quicksight#AnonymousUserDashboardEmbeddingConfigurationDisabledFeature``."""

from typing import Literal, TypeAlias, cast

AnonymousUserDashboardEmbeddingConfigurationDisabledFeature: TypeAlias = Literal[
    "SHARED_VIEW",
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AnonymousUserDashboardEmbeddingConfigurationDisabledFeature,
) -> str:
    return value


def deserialize_json(
    data: str,
) -> AnonymousUserDashboardEmbeddingConfigurationDisabledFeature:
    return cast(AnonymousUserDashboardEmbeddingConfigurationDisabledFeature, data)
