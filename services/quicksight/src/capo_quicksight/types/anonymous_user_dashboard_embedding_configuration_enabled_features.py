"""Generated from Smithy shape ``com.amazonaws.quicksight#AnonymousUserDashboardEmbeddingConfigurationEnabledFeatures``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.anonymous_user_dashboard_embedding_configuration_enabled_feature

AnonymousUserDashboardEmbeddingConfigurationEnabledFeatures: TypeAlias = list[
    "capo_quicksight.types.anonymous_user_dashboard_embedding_configuration_enabled_feature.AnonymousUserDashboardEmbeddingConfigurationEnabledFeature"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AnonymousUserDashboardEmbeddingConfigurationEnabledFeatures,
) -> list:
    import capo_quicksight.types.anonymous_user_dashboard_embedding_configuration_enabled_feature

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.anonymous_user_dashboard_embedding_configuration_enabled_feature.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AnonymousUserDashboardEmbeddingConfigurationEnabledFeatures:
    import capo_quicksight.types.anonymous_user_dashboard_embedding_configuration_enabled_feature

    out: AnonymousUserDashboardEmbeddingConfigurationEnabledFeatures = []
    for item in data:
        out.append(
            capo_quicksight.types.anonymous_user_dashboard_embedding_configuration_enabled_feature.deserialize_json(
                item
            )
        )
    return out
