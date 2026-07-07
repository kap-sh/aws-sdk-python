"""Generated from Smithy shape ``com.amazonaws.firehose#StopDeliveryStreamEncryptionOutput``."""

from typing_extensions import TypedDict


class StopDeliveryStreamEncryptionOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopDeliveryStreamEncryptionOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> StopDeliveryStreamEncryptionOutput:
    out: StopDeliveryStreamEncryptionOutput = {}  # type: ignore[typeddict-item]
    return out
