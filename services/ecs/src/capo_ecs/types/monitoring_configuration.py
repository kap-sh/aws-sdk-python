"""Generated from Smithy shape ``com.amazonaws.ecs#MonitoringConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.metric_configuration_list


class MonitoringConfiguration(TypedDict, closed=True):
    metric_configurations: NotRequired[
        "capo_ecs.types.metric_configuration_list.MetricConfigurationList"
    ]
    """<p>The list of metric configurations for the service monitoring.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonitoringConfiguration) -> dict:
    out: dict = {}
    if "metric_configurations" in value:
        import capo_ecs.types.metric_configuration_list

        out["metricConfigurations"] = (
            capo_ecs.types.metric_configuration_list.serialize_aws_json_1_1(
                value["metric_configurations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MonitoringConfiguration:
    out: MonitoringConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("metricConfigurations") is not None:
        import capo_ecs.types.metric_configuration_list

        out["metric_configurations"] = (
            capo_ecs.types.metric_configuration_list.deserialize_aws_json_1_1(
                data["metricConfigurations"]
            )
        )
    return out
