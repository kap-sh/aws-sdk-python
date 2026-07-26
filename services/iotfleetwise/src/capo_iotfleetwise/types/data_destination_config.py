"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#DataDestinationConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_iotfleetwise.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_iotfleetwise.types.mqtt_topic_config
    import capo_iotfleetwise.types.s3_config
    import capo_iotfleetwise.types.timestream_config


class _DataDestinationConfig_s3Config(TypedDict, closed=True):
    s3Config: "capo_iotfleetwise.types.s3_config.S3Config"


class _DataDestinationConfig_timestreamConfig(TypedDict, closed=True):
    timestreamConfig: "capo_iotfleetwise.types.timestream_config.TimestreamConfig"


class _DataDestinationConfig_mqttTopicConfig(TypedDict, closed=True):
    mqttTopicConfig: "capo_iotfleetwise.types.mqtt_topic_config.MqttTopicConfig"


DataDestinationConfig: TypeAlias = (
    _DataDestinationConfig_s3Config
    | _DataDestinationConfig_timestreamConfig
    | _DataDestinationConfig_mqttTopicConfig
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DataDestinationConfig) -> dict:
    if "s3Config" in value:
        import capo_iotfleetwise.types.s3_config

        return {
            "s3Config": capo_iotfleetwise.types.s3_config.serialize_aws_json_1_0(
                value["s3Config"]
            )
        }
    elif "timestreamConfig" in value:
        import capo_iotfleetwise.types.timestream_config

        return {
            "timestreamConfig": capo_iotfleetwise.types.timestream_config.serialize_aws_json_1_0(
                value["timestreamConfig"]
            )
        }
    elif "mqttTopicConfig" in value:
        import capo_iotfleetwise.types.mqtt_topic_config

        return {
            "mqttTopicConfig": capo_iotfleetwise.types.mqtt_topic_config.serialize_aws_json_1_0(
                value["mqttTopicConfig"]
            )
        }
    else:
        raise SerializationError("DataDestinationConfig: no variant present")


def deserialize_aws_json_1_0(data: dict) -> DataDestinationConfig:
    if "s3Config" in data:
        import capo_iotfleetwise.types.s3_config

        return {
            "s3Config": capo_iotfleetwise.types.s3_config.deserialize_aws_json_1_0(
                data["s3Config"]
            )
        }
    elif "timestreamConfig" in data:
        import capo_iotfleetwise.types.timestream_config

        return {
            "timestreamConfig": capo_iotfleetwise.types.timestream_config.deserialize_aws_json_1_0(
                data["timestreamConfig"]
            )
        }
    elif "mqttTopicConfig" in data:
        import capo_iotfleetwise.types.mqtt_topic_config

        return {
            "mqttTopicConfig": capo_iotfleetwise.types.mqtt_topic_config.deserialize_aws_json_1_0(
                data["mqttTopicConfig"]
            )
        }
    else:
        raise DeserializationError("DataDestinationConfig: no recognized variant key")
