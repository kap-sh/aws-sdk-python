"""Generated from Smithy shape ``com.amazonaws.quicksight#AnonymousUserDashboardEmbeddingConfigurationDisabledFeatures``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.anonymous_user_dashboard_embedding_configuration_disabled_feature

AnonymousUserDashboardEmbeddingConfigurationDisabledFeatures: TypeAlias = list[
    "capo_quicksight.types.anonymous_user_dashboard_embedding_configuration_disabled_feature.AnonymousUserDashboardEmbeddingConfigurationDisabledFeature"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AnonymousUserDashboardEmbeddingConfigurationDisabledFeatures,
) -> list:
    import capo_quicksight.types.anonymous_user_dashboard_embedding_configuration_disabled_feature

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.anonymous_user_dashboard_embedding_configuration_disabled_feature.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AnonymousUserDashboardEmbeddingConfigurationDisabledFeatures:
    import capo_quicksight.types.anonymous_user_dashboard_embedding_configuration_disabled_feature

    out: AnonymousUserDashboardEmbeddingConfigurationDisabledFeatures = []
    for item in data:
        out.append(
            capo_quicksight.types.anonymous_user_dashboard_embedding_configuration_disabled_feature.deserialize_json(
                item
            )
        )
    return out
