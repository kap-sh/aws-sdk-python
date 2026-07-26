"""Generated from Smithy shape ``com.amazonaws.kinesis#DescribeStreamOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis.types.stream_description


class DescribeStreamOutput(TypedDict, closed=True):
    stream_description: "capo_kinesis.types.stream_description.StreamDescription"
    """<p>The current status of the stream, the stream Amazon Resource Name (ARN), an array of shard objects that comprise the stream, and whether there are more shards available.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeStreamOutput) -> dict:
    out: dict = {}
    import capo_kinesis.types.stream_description

    out["StreamDescription"] = (
        capo_kinesis.types.stream_description.serialize_aws_json_1_1(
            value["stream_description"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeStreamOutput:
    out: DescribeStreamOutput = {}  # type: ignore[typeddict-item]
    if "StreamDescription" in data:
        import capo_kinesis.types.stream_description

        out["stream_description"] = (
            capo_kinesis.types.stream_description.deserialize_aws_json_1_1(
                data["StreamDescription"]
            )
        )
    else:
        raise DeserializationError("DescribeStreamOutput.stream_description required")
    return out
