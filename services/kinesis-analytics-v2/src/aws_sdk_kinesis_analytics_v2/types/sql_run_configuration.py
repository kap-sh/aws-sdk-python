"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#SqlRunConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.id
    import aws_sdk_kinesis_analytics_v2.types.input_starting_position_configuration


class SqlRunConfiguration(TypedDict):
    input_id: "aws_sdk_kinesis_analytics_v2.types.id.Id"
    """<p>The input source ID. You can get this ID by calling the <a>DescribeApplication</a> operation. </p>"""
    input_starting_position_configuration: "aws_sdk_kinesis_analytics_v2.types.input_starting_position_configuration.InputStartingPositionConfiguration"
    """<p>The point at which you want the application to start processing records from the streaming source. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SqlRunConfiguration) -> dict:
    out: dict = {}
    out["InputId"] = value["input_id"]
    import aws_sdk_kinesis_analytics_v2.types.input_starting_position_configuration

    out["InputStartingPositionConfiguration"] = (
        aws_sdk_kinesis_analytics_v2.types.input_starting_position_configuration.serialize_aws_json_1_1(
            value["input_starting_position_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SqlRunConfiguration:
    out: SqlRunConfiguration = {}  # type: ignore[typeddict-item]
    if "InputId" in data:
        out["input_id"] = data["InputId"]
    else:
        raise DeserializationError("SqlRunConfiguration.input_id required")
    if "InputStartingPositionConfiguration" in data:
        import aws_sdk_kinesis_analytics_v2.types.input_starting_position_configuration

        out["input_starting_position_configuration"] = (
            aws_sdk_kinesis_analytics_v2.types.input_starting_position_configuration.deserialize_aws_json_1_1(
                data["InputStartingPositionConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "SqlRunConfiguration.input_starting_position_configuration required"
        )
    return out
