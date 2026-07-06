"""Generated from Smithy shape ``com.amazonaws.securityhub#StatelessCustomActionDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.stateless_custom_publish_metric_action


class StatelessCustomActionDefinition(TypedDict, closed=True):
    publish_metric_action: NotRequired[
        "aws_sdk_securityhub.types.stateless_custom_publish_metric_action.StatelessCustomPublishMetricAction"
    ]
    """<p>Information about metrics to publish to CloudWatch.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StatelessCustomActionDefinition) -> dict:
    out: dict = {}
    if "publish_metric_action" in value:
        import aws_sdk_securityhub.types.stateless_custom_publish_metric_action

        out["PublishMetricAction"] = (
            aws_sdk_securityhub.types.stateless_custom_publish_metric_action.serialize_json(
                value["publish_metric_action"]
            )
        )
    return out


def deserialize_json(data: dict) -> StatelessCustomActionDefinition:
    out: StatelessCustomActionDefinition = {}  # type: ignore[typeddict-item]
    if "PublishMetricAction" in data:
        import aws_sdk_securityhub.types.stateless_custom_publish_metric_action

        out["publish_metric_action"] = (
            aws_sdk_securityhub.types.stateless_custom_publish_metric_action.deserialize_json(
                data["PublishMetricAction"]
            )
        )
    return out
