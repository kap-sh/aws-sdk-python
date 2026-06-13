"""Generated from Smithy shape ``com.amazonaws.quicksight#AnonymousUserDashboardEmbeddingConfigurationDisabledFeatures``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.anonymous_user_dashboard_embedding_configuration_disabled_feature

AnonymousUserDashboardEmbeddingConfigurationDisabledFeatures: TypeAlias = list[
    "aws_sdk_quicksight.types.anonymous_user_dashboard_embedding_configuration_disabled_feature.AnonymousUserDashboardEmbeddingConfigurationDisabledFeature"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AnonymousUserDashboardEmbeddingConfigurationDisabledFeatures,
) -> list:
    import aws_sdk_quicksight.types.anonymous_user_dashboard_embedding_configuration_disabled_feature

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.anonymous_user_dashboard_embedding_configuration_disabled_feature.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AnonymousUserDashboardEmbeddingConfigurationDisabledFeatures:
    import aws_sdk_quicksight.types.anonymous_user_dashboard_embedding_configuration_disabled_feature

    out: AnonymousUserDashboardEmbeddingConfigurationDisabledFeatures = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.anonymous_user_dashboard_embedding_configuration_disabled_feature.deserialize_json(
                item
            )
        )
    return out
