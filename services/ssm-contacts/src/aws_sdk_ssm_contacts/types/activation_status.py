"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ActivationStatus``."""

from typing import Literal, TypeAlias, cast

ActivationStatus: TypeAlias = Literal[
    "ACTIVATED",
    "NOT_ACTIVATED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActivationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ActivationStatus:
    return cast(ActivationStatus, data)
