"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#LogDeliveryConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_timestream_influxdb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_timestream_influxdb.types.s3_configuration


class LogDeliveryConfiguration(TypedDict, closed=True):
    s3_configuration: (
        "aws_sdk_timestream_influxdb.types.s3_configuration.S3Configuration"
    )
    """<p>Configuration for S3 bucket log delivery.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LogDeliveryConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_timestream_influxdb.types.s3_configuration

    out["s3Configuration"] = (
        aws_sdk_timestream_influxdb.types.s3_configuration.serialize_aws_json_1_0(
            value["s3_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> LogDeliveryConfiguration:
    out: LogDeliveryConfiguration = {}  # type: ignore[typeddict-item]
    if "s3Configuration" in data:
        import aws_sdk_timestream_influxdb.types.s3_configuration

        out["s3_configuration"] = (
            aws_sdk_timestream_influxdb.types.s3_configuration.deserialize_aws_json_1_0(
                data["s3Configuration"]
            )
        )
    else:
        raise DeserializationError("LogDeliveryConfiguration.s3_configuration required")
    return out
