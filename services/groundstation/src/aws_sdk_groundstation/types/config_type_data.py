"""Generated from Smithy shape ``com.amazonaws.groundstation#ConfigTypeData``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_groundstation.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.antenna_downlink_config
    import aws_sdk_groundstation.types.antenna_downlink_demod_decode_config
    import aws_sdk_groundstation.types.antenna_uplink_config
    import aws_sdk_groundstation.types.dataflow_endpoint_config
    import aws_sdk_groundstation.types.s3_recording_config
    import aws_sdk_groundstation.types.telemetry_sink_config
    import aws_sdk_groundstation.types.tracking_config
    import aws_sdk_groundstation.types.uplink_echo_config


class _ConfigTypeData_antennaDownlinkConfig(TypedDict):
    antennaDownlinkConfig: (
        "aws_sdk_groundstation.types.antenna_downlink_config.AntennaDownlinkConfig"
    )


class _ConfigTypeData_trackingConfig(TypedDict):
    trackingConfig: "aws_sdk_groundstation.types.tracking_config.TrackingConfig"


class _ConfigTypeData_dataflowEndpointConfig(TypedDict):
    dataflowEndpointConfig: (
        "aws_sdk_groundstation.types.dataflow_endpoint_config.DataflowEndpointConfig"
    )


class _ConfigTypeData_antennaDownlinkDemodDecodeConfig(TypedDict):
    antennaDownlinkDemodDecodeConfig: "aws_sdk_groundstation.types.antenna_downlink_demod_decode_config.AntennaDownlinkDemodDecodeConfig"


class _ConfigTypeData_antennaUplinkConfig(TypedDict):
    antennaUplinkConfig: (
        "aws_sdk_groundstation.types.antenna_uplink_config.AntennaUplinkConfig"
    )


class _ConfigTypeData_uplinkEchoConfig(TypedDict):
    uplinkEchoConfig: "aws_sdk_groundstation.types.uplink_echo_config.UplinkEchoConfig"


class _ConfigTypeData_s3RecordingConfig(TypedDict):
    s3RecordingConfig: (
        "aws_sdk_groundstation.types.s3_recording_config.S3RecordingConfig"
    )


class _ConfigTypeData_telemetrySinkConfig(TypedDict):
    telemetrySinkConfig: (
        "aws_sdk_groundstation.types.telemetry_sink_config.TelemetrySinkConfig"
    )


ConfigTypeData: TypeAlias = (
    _ConfigTypeData_antennaDownlinkConfig
    | _ConfigTypeData_trackingConfig
    | _ConfigTypeData_dataflowEndpointConfig
    | _ConfigTypeData_antennaDownlinkDemodDecodeConfig
    | _ConfigTypeData_antennaUplinkConfig
    | _ConfigTypeData_uplinkEchoConfig
    | _ConfigTypeData_s3RecordingConfig
    | _ConfigTypeData_telemetrySinkConfig
)


# --- restJson1 ser/de ---
def serialize_json(value: ConfigTypeData) -> dict:
    if "antennaDownlinkConfig" in value:
        import aws_sdk_groundstation.types.antenna_downlink_config

        return {
            "antennaDownlinkConfig": aws_sdk_groundstation.types.antenna_downlink_config.serialize_json(
                value["antennaDownlinkConfig"]
            )
        }
    elif "trackingConfig" in value:
        import aws_sdk_groundstation.types.tracking_config

        return {
            "trackingConfig": aws_sdk_groundstation.types.tracking_config.serialize_json(
                value["trackingConfig"]
            )
        }
    elif "dataflowEndpointConfig" in value:
        import aws_sdk_groundstation.types.dataflow_endpoint_config

        return {
            "dataflowEndpointConfig": aws_sdk_groundstation.types.dataflow_endpoint_config.serialize_json(
                value["dataflowEndpointConfig"]
            )
        }
    elif "antennaDownlinkDemodDecodeConfig" in value:
        import aws_sdk_groundstation.types.antenna_downlink_demod_decode_config

        return {
            "antennaDownlinkDemodDecodeConfig": aws_sdk_groundstation.types.antenna_downlink_demod_decode_config.serialize_json(
                value["antennaDownlinkDemodDecodeConfig"]
            )
        }
    elif "antennaUplinkConfig" in value:
        import aws_sdk_groundstation.types.antenna_uplink_config

        return {
            "antennaUplinkConfig": aws_sdk_groundstation.types.antenna_uplink_config.serialize_json(
                value["antennaUplinkConfig"]
            )
        }
    elif "uplinkEchoConfig" in value:
        import aws_sdk_groundstation.types.uplink_echo_config

        return {
            "uplinkEchoConfig": aws_sdk_groundstation.types.uplink_echo_config.serialize_json(
                value["uplinkEchoConfig"]
            )
        }
    elif "s3RecordingConfig" in value:
        import aws_sdk_groundstation.types.s3_recording_config

        return {
            "s3RecordingConfig": aws_sdk_groundstation.types.s3_recording_config.serialize_json(
                value["s3RecordingConfig"]
            )
        }
    elif "telemetrySinkConfig" in value:
        import aws_sdk_groundstation.types.telemetry_sink_config

        return {
            "telemetrySinkConfig": aws_sdk_groundstation.types.telemetry_sink_config.serialize_json(
                value["telemetrySinkConfig"]
            )
        }
    else:
        raise SerializationError("ConfigTypeData: no variant present")


def deserialize_json(data: dict) -> ConfigTypeData:
    if "antennaDownlinkConfig" in data:
        import aws_sdk_groundstation.types.antenna_downlink_config

        return {
            "antennaDownlinkConfig": aws_sdk_groundstation.types.antenna_downlink_config.deserialize_json(
                data["antennaDownlinkConfig"]
            )
        }
    elif "trackingConfig" in data:
        import aws_sdk_groundstation.types.tracking_config

        return {
            "trackingConfig": aws_sdk_groundstation.types.tracking_config.deserialize_json(
                data["trackingConfig"]
            )
        }
    elif "dataflowEndpointConfig" in data:
        import aws_sdk_groundstation.types.dataflow_endpoint_config

        return {
            "dataflowEndpointConfig": aws_sdk_groundstation.types.dataflow_endpoint_config.deserialize_json(
                data["dataflowEndpointConfig"]
            )
        }
    elif "antennaDownlinkDemodDecodeConfig" in data:
        import aws_sdk_groundstation.types.antenna_downlink_demod_decode_config

        return {
            "antennaDownlinkDemodDecodeConfig": aws_sdk_groundstation.types.antenna_downlink_demod_decode_config.deserialize_json(
                data["antennaDownlinkDemodDecodeConfig"]
            )
        }
    elif "antennaUplinkConfig" in data:
        import aws_sdk_groundstation.types.antenna_uplink_config

        return {
            "antennaUplinkConfig": aws_sdk_groundstation.types.antenna_uplink_config.deserialize_json(
                data["antennaUplinkConfig"]
            )
        }
    elif "uplinkEchoConfig" in data:
        import aws_sdk_groundstation.types.uplink_echo_config

        return {
            "uplinkEchoConfig": aws_sdk_groundstation.types.uplink_echo_config.deserialize_json(
                data["uplinkEchoConfig"]
            )
        }
    elif "s3RecordingConfig" in data:
        import aws_sdk_groundstation.types.s3_recording_config

        return {
            "s3RecordingConfig": aws_sdk_groundstation.types.s3_recording_config.deserialize_json(
                data["s3RecordingConfig"]
            )
        }
    elif "telemetrySinkConfig" in data:
        import aws_sdk_groundstation.types.telemetry_sink_config

        return {
            "telemetrySinkConfig": aws_sdk_groundstation.types.telemetry_sink_config.deserialize_json(
                data["telemetrySinkConfig"]
            )
        }
    else:
        raise DeserializationError("ConfigTypeData: no recognized variant key")
