"""Generated from Smithy shape ``com.amazonaws.firehose#DeleteDeliveryStreamOutput``."""

from typing_extensions import TypedDict


class DeleteDeliveryStreamOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDeliveryStreamOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDeliveryStreamOutput:
    out: DeleteDeliveryStreamOutput = {}  # type: ignore[typeddict-item]
    return out
