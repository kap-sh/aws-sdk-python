"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#CheckpointConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.boolean_object
    import aws_sdk_kinesis_analytics_v2.types.checkpoint_interval
    import aws_sdk_kinesis_analytics_v2.types.configuration_type
    import aws_sdk_kinesis_analytics_v2.types.min_pause_between_checkpoints


class CheckpointConfiguration(TypedDict):
    configuration_type: (
        "aws_sdk_kinesis_analytics_v2.types.configuration_type.ConfigurationType"
    )
    """<p>Describes whether the application uses Managed Service for Apache Flink' default checkpointing behavior. You must set this property to <code>CUSTOM</code> in order to set the <code>CheckpointingEnabled</code>, <code>CheckpointInterval</code>, or <code>MinPauseBetweenCheckpoints</code> parameters.</p> <note> <p>If this value is set to <code>DEFAULT</code>, the application will use the following values, even if they are set to other values using APIs or application code:</p> <ul> <li> <p> <b>CheckpointingEnabled:</b> true</p> </li> <li> <p> <b>CheckpointInterval:</b> 60000</p> </li> <li> <p> <b>MinPauseBetweenCheckpoints:</b> 5000</p> </li> </ul> </note>"""
    checkpointing_enabled: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.boolean_object.BooleanObject"
    ]
    """<p>Describes whether checkpointing is enabled for a Managed Service for Apache Flink application.</p> <note> <p>If <code>CheckpointConfiguration.ConfigurationType</code> is <code>DEFAULT</code>, the application will use a <code>CheckpointingEnabled</code> value of <code>true</code>, even if this value is set to another value using this API or in application code.</p> </note>"""
    checkpoint_interval: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.checkpoint_interval.CheckpointInterval"
    ]
    """<p>Describes the interval in milliseconds between checkpoint operations. </p> <note> <p>If <code>CheckpointConfiguration.ConfigurationType</code> is <code>DEFAULT</code>, the application will use a <code>CheckpointInterval</code> value of 60000, even if this value is set to another value using this API or in application code.</p> </note>"""
    min_pause_between_checkpoints: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.min_pause_between_checkpoints.MinPauseBetweenCheckpoints"
    ]
    """<p>Describes the minimum time in milliseconds after a checkpoint operation completes that a new checkpoint operation can start. If a checkpoint operation takes longer than the <code>CheckpointInterval</code>, the application otherwise performs continual checkpoint operations. For more information, see <a href=\"https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/ops/state/large_state_tuning/#tuning-checkpointing\"> Tuning Checkpointing</a> in the <a href=\"https://nightlies.apache.org/flink/flink-docs-release-2.2/\">Apache Flink Documentation</a>.</p> <note> <p>If <code>CheckpointConfiguration.ConfigurationType</code> is <code>DEFAULT</code>, the application will use a <code>MinPauseBetweenCheckpoints</code> value of 5000, even if this value is set using this API or in application code.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CheckpointConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_kinesis_analytics_v2.types.configuration_type

    out["ConfigurationType"] = (
        aws_sdk_kinesis_analytics_v2.types.configuration_type.serialize_aws_json_1_1(
            value["configuration_type"]
        )
    )
    if "checkpointing_enabled" in value:
        out["CheckpointingEnabled"] = value["checkpointing_enabled"]
    if "checkpoint_interval" in value:
        out["CheckpointInterval"] = value["checkpoint_interval"]
    if "min_pause_between_checkpoints" in value:
        out["MinPauseBetweenCheckpoints"] = value["min_pause_between_checkpoints"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CheckpointConfiguration:
    out: CheckpointConfiguration = {}  # type: ignore[typeddict-item]
    if "ConfigurationType" in data:
        import aws_sdk_kinesis_analytics_v2.types.configuration_type

        out["configuration_type"] = (
            aws_sdk_kinesis_analytics_v2.types.configuration_type.deserialize_aws_json_1_1(
                data["ConfigurationType"]
            )
        )
    else:
        raise DeserializationError(
            "CheckpointConfiguration.configuration_type required"
        )
    if "CheckpointingEnabled" in data:
        out["checkpointing_enabled"] = data["CheckpointingEnabled"]
    if "CheckpointInterval" in data:
        out["checkpoint_interval"] = data["CheckpointInterval"]
    if "MinPauseBetweenCheckpoints" in data:
        out["min_pause_between_checkpoints"] = data["MinPauseBetweenCheckpoints"]
    return out
