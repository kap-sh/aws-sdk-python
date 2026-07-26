"""Generated from Smithy shape ``com.amazonaws.securityhub#StatelessCustomPublishMetricActionDimensionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.stateless_custom_publish_metric_action_dimension

StatelessCustomPublishMetricActionDimensionsList: TypeAlias = list[
    "capo_securityhub.types.stateless_custom_publish_metric_action_dimension.StatelessCustomPublishMetricActionDimension"
]


# --- restJson1 ser/de ---
def serialize_json(value: StatelessCustomPublishMetricActionDimensionsList) -> list:
    import capo_securityhub.types.stateless_custom_publish_metric_action_dimension

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.stateless_custom_publish_metric_action_dimension.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> StatelessCustomPublishMetricActionDimensionsList:
    import capo_securityhub.types.stateless_custom_publish_metric_action_dimension

    out: StatelessCustomPublishMetricActionDimensionsList = []
    for item in data:
        out.append(
            capo_securityhub.types.stateless_custom_publish_metric_action_dimension.deserialize_json(
                item
            )
        )
    return out
