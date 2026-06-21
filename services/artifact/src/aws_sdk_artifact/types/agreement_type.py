"""Generated from Smithy shape ``com.amazonaws.artifact#AgreementType``."""

from typing import Literal, TypeAlias, cast

AgreementType: TypeAlias = Literal[
    "CUSTOM",
    "DEFAULT",
    "MODIFIED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AgreementType) -> str:
    return value


def deserialize_json(data: str) -> AgreementType:
    return cast(AgreementType, data)
