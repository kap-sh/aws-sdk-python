"""Generated from Smithy shape ``com.amazonaws.securityhub#StatelessCustomPublishMetricAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.stateless_custom_publish_metric_action_dimensions_list


class StatelessCustomPublishMetricAction(TypedDict, closed=True):
    dimensions: NotRequired[
        "capo_securityhub.types.stateless_custom_publish_metric_action_dimensions_list.StatelessCustomPublishMetricActionDimensionsList"
    ]
    """<p>Defines CloudWatch dimension values to publish.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StatelessCustomPublishMetricAction) -> dict:
    out: dict = {}
    if "dimensions" in value:
        import capo_securityhub.types.stateless_custom_publish_metric_action_dimensions_list

        out["Dimensions"] = (
            capo_securityhub.types.stateless_custom_publish_metric_action_dimensions_list.serialize_json(
                value["dimensions"]
            )
        )
    return out


def deserialize_json(data: dict) -> StatelessCustomPublishMetricAction:
    out: StatelessCustomPublishMetricAction = {}  # type: ignore[typeddict-item]
    if "Dimensions" in data:
        import capo_securityhub.types.stateless_custom_publish_metric_action_dimensions_list

        out["dimensions"] = (
            capo_securityhub.types.stateless_custom_publish_metric_action_dimensions_list.deserialize_json(
                data["Dimensions"]
            )
        )
    return out
