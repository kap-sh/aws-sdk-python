"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#FlinkApplicationConfigurationUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.checkpoint_configuration_update
    import capo_kinesis_analytics_v2.types.monitoring_configuration_update
    import capo_kinesis_analytics_v2.types.parallelism_configuration_update


class FlinkApplicationConfigurationUpdate(TypedDict, closed=True):
    checkpoint_configuration_update: NotRequired[
        "capo_kinesis_analytics_v2.types.checkpoint_configuration_update.CheckpointConfigurationUpdate"
    ]
    """<p>Describes updates to an application's checkpointing configuration. Checkpointing is the process of persisting application state for fault tolerance.</p>"""
    monitoring_configuration_update: NotRequired[
        "capo_kinesis_analytics_v2.types.monitoring_configuration_update.MonitoringConfigurationUpdate"
    ]
    """<p>Describes updates to the configuration parameters for Amazon CloudWatch logging for an application.</p>"""
    parallelism_configuration_update: NotRequired[
        "capo_kinesis_analytics_v2.types.parallelism_configuration_update.ParallelismConfigurationUpdate"
    ]
    """<p>Describes updates to the parameters for how an application executes multiple tasks simultaneously.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FlinkApplicationConfigurationUpdate) -> dict:
    out: dict = {}
    if "checkpoint_configuration_update" in value:
        import capo_kinesis_analytics_v2.types.checkpoint_configuration_update

        out["CheckpointConfigurationUpdate"] = (
            capo_kinesis_analytics_v2.types.checkpoint_configuration_update.serialize_aws_json_1_1(
                value["checkpoint_configuration_update"]
            )
        )
    if "monitoring_configuration_update" in value:
        import capo_kinesis_analytics_v2.types.monitoring_configuration_update

        out["MonitoringConfigurationUpdate"] = (
            capo_kinesis_analytics_v2.types.monitoring_configuration_update.serialize_aws_json_1_1(
                value["monitoring_configuration_update"]
            )
        )
    if "parallelism_configuration_update" in value:
        import capo_kinesis_analytics_v2.types.parallelism_configuration_update

        out["ParallelismConfigurationUpdate"] = (
            capo_kinesis_analytics_v2.types.parallelism_configuration_update.serialize_aws_json_1_1(
                value["parallelism_configuration_update"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FlinkApplicationConfigurationUpdate:
    out: FlinkApplicationConfigurationUpdate = {}  # type: ignore[typeddict-item]
    if "CheckpointConfigurationUpdate" in data:
        import capo_kinesis_analytics_v2.types.checkpoint_configuration_update

        out["checkpoint_configuration_update"] = (
            capo_kinesis_analytics_v2.types.checkpoint_configuration_update.deserialize_aws_json_1_1(
                data["CheckpointConfigurationUpdate"]
            )
        )
    if "MonitoringConfigurationUpdate" in data:
        import capo_kinesis_analytics_v2.types.monitoring_configuration_update

        out["monitoring_configuration_update"] = (
            capo_kinesis_analytics_v2.types.monitoring_configuration_update.deserialize_aws_json_1_1(
                data["MonitoringConfigurationUpdate"]
            )
        )
    if "ParallelismConfigurationUpdate" in data:
        import capo_kinesis_analytics_v2.types.parallelism_configuration_update

        out["parallelism_configuration_update"] = (
            capo_kinesis_analytics_v2.types.parallelism_configuration_update.deserialize_aws_json_1_1(
                data["ParallelismConfigurationUpdate"]
            )
        )
    return out
