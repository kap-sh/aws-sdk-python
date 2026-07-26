"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#LegalDocumentType``."""

from typing import Literal, TypeAlias, cast

LegalDocumentType: TypeAlias = Literal[
    "CustomEula",
    "CustomDsa",
    "EnterpriseEula",
    "StandardEula",
    "StandardDsa",
]


# --- restJson1 ser/de ---
def serialize_json(value: LegalDocumentType) -> str:
    return value


def deserialize_json(data: str) -> LegalDocumentType:
    return cast(LegalDocumentType, data)
