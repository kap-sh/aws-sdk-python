"""Generated from Smithy shape ``com.amazonaws.firehose#StartDeliveryStreamEncryptionOutput``."""

from typing_extensions import TypedDict


class StartDeliveryStreamEncryptionOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartDeliveryStreamEncryptionOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> StartDeliveryStreamEncryptionOutput:
    out: StartDeliveryStreamEncryptionOutput = {}  # type: ignore[typeddict-item]
    return out
