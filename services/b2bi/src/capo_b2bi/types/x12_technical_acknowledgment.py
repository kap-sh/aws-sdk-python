"""Generated from Smithy shape ``com.amazonaws.b2bi#X12TechnicalAcknowledgment``."""

from typing import Literal, TypeAlias, cast

X12TechnicalAcknowledgment: TypeAlias = Literal[
    "DO_NOT_GENERATE",
    "GENERATE_ALL_SEGMENTS",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: X12TechnicalAcknowledgment) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> X12TechnicalAcknowledgment:
    return cast(X12TechnicalAcknowledgment, data)
