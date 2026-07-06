"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#Parameters``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_timestream_influxdb.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_timestream_influxdb.types.influx_d_bv2_parameters
    import aws_sdk_timestream_influxdb.types.influx_d_bv3_core_parameters
    import aws_sdk_timestream_influxdb.types.influx_d_bv3_enterprise_parameters


class _Parameters_InfluxDBv2(TypedDict, closed=True):
    InfluxDBv2: (
        "aws_sdk_timestream_influxdb.types.influx_d_bv2_parameters.InfluxDBv2Parameters"
    )


class _Parameters_InfluxDBv3Core(TypedDict, closed=True):
    InfluxDBv3Core: "aws_sdk_timestream_influxdb.types.influx_d_bv3_core_parameters.InfluxDBv3CoreParameters"


class _Parameters_InfluxDBv3Enterprise(TypedDict, closed=True):
    InfluxDBv3Enterprise: "aws_sdk_timestream_influxdb.types.influx_d_bv3_enterprise_parameters.InfluxDBv3EnterpriseParameters"


Parameters: TypeAlias = (
    _Parameters_InfluxDBv2
    | _Parameters_InfluxDBv3Core
    | _Parameters_InfluxDBv3Enterprise
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Parameters) -> dict:
    if "InfluxDBv2" in value:
        import aws_sdk_timestream_influxdb.types.influx_d_bv2_parameters

        return {
            "InfluxDBv2": aws_sdk_timestream_influxdb.types.influx_d_bv2_parameters.serialize_aws_json_1_0(
                value["InfluxDBv2"]
            )
        }
    elif "InfluxDBv3Core" in value:
        import aws_sdk_timestream_influxdb.types.influx_d_bv3_core_parameters

        return {
            "InfluxDBv3Core": aws_sdk_timestream_influxdb.types.influx_d_bv3_core_parameters.serialize_aws_json_1_0(
                value["InfluxDBv3Core"]
            )
        }
    elif "InfluxDBv3Enterprise" in value:
        import aws_sdk_timestream_influxdb.types.influx_d_bv3_enterprise_parameters

        return {
            "InfluxDBv3Enterprise": aws_sdk_timestream_influxdb.types.influx_d_bv3_enterprise_parameters.serialize_aws_json_1_0(
                value["InfluxDBv3Enterprise"]
            )
        }
    else:
        raise SerializationError("Parameters: no variant present")


def deserialize_aws_json_1_0(data: dict) -> Parameters:
    if "InfluxDBv2" in data:
        import aws_sdk_timestream_influxdb.types.influx_d_bv2_parameters

        return {
            "InfluxDBv2": aws_sdk_timestream_influxdb.types.influx_d_bv2_parameters.deserialize_aws_json_1_0(
                data["InfluxDBv2"]
            )
        }
    elif "InfluxDBv3Core" in data:
        import aws_sdk_timestream_influxdb.types.influx_d_bv3_core_parameters

        return {
            "InfluxDBv3Core": aws_sdk_timestream_influxdb.types.influx_d_bv3_core_parameters.deserialize_aws_json_1_0(
                data["InfluxDBv3Core"]
            )
        }
    elif "InfluxDBv3Enterprise" in data:
        import aws_sdk_timestream_influxdb.types.influx_d_bv3_enterprise_parameters

        return {
            "InfluxDBv3Enterprise": aws_sdk_timestream_influxdb.types.influx_d_bv3_enterprise_parameters.deserialize_aws_json_1_0(
                data["InfluxDBv3Enterprise"]
            )
        }
    else:
        raise DeserializationError("Parameters: no recognized variant key")
