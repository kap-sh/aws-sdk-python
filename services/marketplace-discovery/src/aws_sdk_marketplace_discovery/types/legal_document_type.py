"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#LegalDocumentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_discovery.errors import DeserializationError

LegalDocumentType: TypeAlias = Literal[
    "CustomEula",
    "CustomDsa",
    "EnterpriseEula",
    "StandardEula",
    "StandardDsa",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CustomEula",
        "CustomDsa",
        "EnterpriseEula",
        "StandardEula",
        "StandardDsa",
    )
)


def serialize_json(value: LegalDocumentType) -> str:
    return value


def deserialize_json(data: str) -> LegalDocumentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LegalDocumentType value: {data!r}")
    return cast(LegalDocumentType, data)
