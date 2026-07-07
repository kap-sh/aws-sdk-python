"""Generated from Smithy shape ``com.amazonaws.firehose#UntagDeliveryStreamOutput``."""

from typing_extensions import TypedDict


class UntagDeliveryStreamOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagDeliveryStreamOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagDeliveryStreamOutput:
    out: UntagDeliveryStreamOutput = {}  # type: ignore[typeddict-item]
    return out
