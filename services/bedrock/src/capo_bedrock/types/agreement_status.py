"""Generated from Smithy shape ``com.amazonaws.bedrock#AgreementStatus``."""

from typing import Literal, TypeAlias, cast

AgreementStatus: TypeAlias = Literal[
    "AVAILABLE",
    "PENDING",
    "NOT_AVAILABLE",
    "ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: AgreementStatus) -> str:
    return value


def deserialize_json(data: str) -> AgreementStatus:
    return cast(AgreementStatus, data)
