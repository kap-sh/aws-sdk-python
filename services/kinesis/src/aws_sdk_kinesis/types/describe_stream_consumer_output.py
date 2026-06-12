"""Generated from Smithy shape ``com.amazonaws.kinesis#DescribeStreamConsumerOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis.types.consumer_description


class DescribeStreamConsumerOutput(TypedDict):
    consumer_description: (
        "aws_sdk_kinesis.types.consumer_description.ConsumerDescription"
    )
    """<p>An object that represents the details of the consumer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeStreamConsumerOutput) -> dict:
    out: dict = {}
    import aws_sdk_kinesis.types.consumer_description

    out["ConsumerDescription"] = (
        aws_sdk_kinesis.types.consumer_description.serialize_aws_json_1_1(
            value["consumer_description"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeStreamConsumerOutput:
    out: DescribeStreamConsumerOutput = {}  # type: ignore[typeddict-item]
    if "ConsumerDescription" in data:
        import aws_sdk_kinesis.types.consumer_description

        out["consumer_description"] = (
            aws_sdk_kinesis.types.consumer_description.deserialize_aws_json_1_1(
                data["ConsumerDescription"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeStreamConsumerOutput.consumer_description required"
        )
    return out
