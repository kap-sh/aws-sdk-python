"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#InputStartingPositionConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics.types.input_starting_position


class InputStartingPositionConfiguration(TypedDict):
    input_starting_position: NotRequired[
        "aws_sdk_kinesis_analytics.types.input_starting_position.InputStartingPosition"
    ]
    """<p>The starting position on the stream.</p> <ul> <li> <p> <code>NOW</code> - Start reading just after the most recent record in the stream, start at the request time stamp that the customer issued.</p> </li> <li> <p> <code>TRIM_HORIZON</code> - Start reading at the last untrimmed record in the stream, which is the oldest record available in the stream. This option is not available for an Amazon Kinesis Firehose delivery stream.</p> </li> <li> <p> <code>LAST_STOPPED_POINT</code> - Resume reading from where the application last stopped reading.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputStartingPositionConfiguration) -> dict:
    out: dict = {}
    if "input_starting_position" in value:
        import aws_sdk_kinesis_analytics.types.input_starting_position

        out["InputStartingPosition"] = (
            aws_sdk_kinesis_analytics.types.input_starting_position.serialize_aws_json_1_1(
                value["input_starting_position"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InputStartingPositionConfiguration:
    out: InputStartingPositionConfiguration = {}  # type: ignore[typeddict-item]
    if "InputStartingPosition" in data:
        import aws_sdk_kinesis_analytics.types.input_starting_position

        out["input_starting_position"] = (
            aws_sdk_kinesis_analytics.types.input_starting_position.deserialize_aws_json_1_1(
                data["InputStartingPosition"]
            )
        )
    return out
