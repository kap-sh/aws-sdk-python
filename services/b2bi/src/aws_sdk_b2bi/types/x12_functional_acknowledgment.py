"""Generated from Smithy shape ``com.amazonaws.b2bi#X12FunctionalAcknowledgment``."""

from typing import Literal, TypeAlias, cast

X12FunctionalAcknowledgment: TypeAlias = Literal[
    "DO_NOT_GENERATE",
    "GENERATE_ALL_SEGMENTS",
    "GENERATE_WITHOUT_TRANSACTION_SET_RESPONSE_LOOP",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: X12FunctionalAcknowledgment) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> X12FunctionalAcknowledgment:
    return cast(X12FunctionalAcknowledgment, data)
