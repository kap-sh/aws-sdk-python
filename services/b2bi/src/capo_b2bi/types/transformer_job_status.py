"""Generated from Smithy shape ``com.amazonaws.b2bi#TransformerJobStatus``."""

from typing import Literal, TypeAlias, cast

TransformerJobStatus: TypeAlias = Literal[
    "running",
    "succeeded",
    "failed",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TransformerJobStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> TransformerJobStatus:
    return cast(TransformerJobStatus, data)
