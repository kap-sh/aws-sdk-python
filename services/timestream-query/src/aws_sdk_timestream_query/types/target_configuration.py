"""Generated from Smithy shape ``com.amazonaws.timestreamquery#TargetConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_timestream_query.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_timestream_query.types.timestream_configuration


class TargetConfiguration(TypedDict):
    timestream_configuration: "aws_sdk_timestream_query.types.timestream_configuration.TimestreamConfiguration"
    """<p>Configuration needed to write data into the Timestream database and table.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TargetConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_timestream_query.types.timestream_configuration

    out["TimestreamConfiguration"] = (
        aws_sdk_timestream_query.types.timestream_configuration.serialize_aws_json_1_0(
            value["timestream_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> TargetConfiguration:
    out: TargetConfiguration = {}  # type: ignore[typeddict-item]
    if "TimestreamConfiguration" in data:
        import aws_sdk_timestream_query.types.timestream_configuration

        out["timestream_configuration"] = (
            aws_sdk_timestream_query.types.timestream_configuration.deserialize_aws_json_1_0(
                data["TimestreamConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "TargetConfiguration.timestream_configuration required"
        )
    return out
