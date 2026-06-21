"""Generated from Smithy shape ``com.amazonaws.transcribe#OutputLocationType``."""

from typing import Literal, TypeAlias, cast

OutputLocationType: TypeAlias = Literal[
    "CUSTOMER_BUCKET",
    "SERVICE_BUCKET",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OutputLocationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OutputLocationType:
    return cast(OutputLocationType, data)
