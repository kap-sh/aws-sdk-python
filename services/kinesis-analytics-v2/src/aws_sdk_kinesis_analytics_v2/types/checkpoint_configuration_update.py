"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#CheckpointConfigurationUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.boolean_object
    import aws_sdk_kinesis_analytics_v2.types.checkpoint_interval
    import aws_sdk_kinesis_analytics_v2.types.configuration_type
    import aws_sdk_kinesis_analytics_v2.types.min_pause_between_checkpoints


class CheckpointConfigurationUpdate(TypedDict, closed=True):
    configuration_type_update: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.configuration_type.ConfigurationType"
    ]
    """<p>Describes updates to whether the application uses the default checkpointing behavior of Managed Service for Apache Flink. You must set this property to <code>CUSTOM</code> in order to set the <code>CheckpointingEnabled</code>, <code>CheckpointInterval</code>, or <code>MinPauseBetweenCheckpoints</code> parameters. </p> <note> <p>If this value is set to <code>DEFAULT</code>, the application will use the following values, even if they are set to other values using APIs or application code:</p> <ul> <li> <p> <b>CheckpointingEnabled:</b> true</p> </li> <li> <p> <b>CheckpointInterval:</b> 60000</p> </li> <li> <p> <b>MinPauseBetweenCheckpoints:</b> 5000</p> </li> </ul> </note>"""
    checkpointing_enabled_update: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.boolean_object.BooleanObject"
    ]
    """<p>Describes updates to whether checkpointing is enabled for an application.</p> <note> <p>If <code>CheckpointConfiguration.ConfigurationType</code> is <code>DEFAULT</code>, the application will use a <code>CheckpointingEnabled</code> value of <code>true</code>, even if this value is set to another value using this API or in application code.</p> </note>"""
    checkpoint_interval_update: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.checkpoint_interval.CheckpointInterval"
    ]
    """<p>Describes updates to the interval in milliseconds between checkpoint operations.</p> <note> <p>If <code>CheckpointConfiguration.ConfigurationType</code> is <code>DEFAULT</code>, the application will use a <code>CheckpointInterval</code> value of 60000, even if this value is set to another value using this API or in application code.</p> </note>"""
    min_pause_between_checkpoints_update: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.min_pause_between_checkpoints.MinPauseBetweenCheckpoints"
    ]
    """<p>Describes updates to the minimum time in milliseconds after a checkpoint operation completes that a new checkpoint operation can start.</p> <note> <p>If <code>CheckpointConfiguration.ConfigurationType</code> is <code>DEFAULT</code>, the application will use a <code>MinPauseBetweenCheckpoints</code> value of 5000, even if this value is set using this API or in application code.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CheckpointConfigurationUpdate) -> dict:
    out: dict = {}
    if "configuration_type_update" in value:
        import aws_sdk_kinesis_analytics_v2.types.configuration_type

        out["ConfigurationTypeUpdate"] = (
            aws_sdk_kinesis_analytics_v2.types.configuration_type.serialize_aws_json_1_1(
                value["configuration_type_update"]
            )
        )
    if "checkpointing_enabled_update" in value:
        out["CheckpointingEnabledUpdate"] = value["checkpointing_enabled_update"]
    if "checkpoint_interval_update" in value:
        out["CheckpointIntervalUpdate"] = value["checkpoint_interval_update"]
    if "min_pause_between_checkpoints_update" in value:
        out["MinPauseBetweenCheckpointsUpdate"] = value[
            "min_pause_between_checkpoints_update"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> CheckpointConfigurationUpdate:
    out: CheckpointConfigurationUpdate = {}  # type: ignore[typeddict-item]
    if "ConfigurationTypeUpdate" in data:
        import aws_sdk_kinesis_analytics_v2.types.configuration_type

        out["configuration_type_update"] = (
            aws_sdk_kinesis_analytics_v2.types.configuration_type.deserialize_aws_json_1_1(
                data["ConfigurationTypeUpdate"]
            )
        )
    if "CheckpointingEnabledUpdate" in data:
        out["checkpointing_enabled_update"] = data["CheckpointingEnabledUpdate"]
    if "CheckpointIntervalUpdate" in data:
        out["checkpoint_interval_update"] = data["CheckpointIntervalUpdate"]
    if "MinPauseBetweenCheckpointsUpdate" in data:
        out["min_pause_between_checkpoints_update"] = data[
            "MinPauseBetweenCheckpointsUpdate"
        ]
    return out
