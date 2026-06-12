"""Generated from Smithy shape ``com.amazonaws.macie2#SensitiveDataItemCategory``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

"""<p>For a finding, the category of sensitive data that was detected and produced the finding. For a managed data identifier, the category of sensitive data that the managed data identifier detects. Possible values are:</p>"""
SensitiveDataItemCategory: TypeAlias = Literal[
    "FINANCIAL_INFORMATION",
    "PERSONAL_INFORMATION",
    "CREDENTIALS",
    "CUSTOM_IDENTIFIER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FINANCIAL_INFORMATION",
        "PERSONAL_INFORMATION",
        "CREDENTIALS",
        "CUSTOM_IDENTIFIER",
    )
)


def serialize_json(value: SensitiveDataItemCategory) -> str:
    return value


def deserialize_json(data: str) -> SensitiveDataItemCategory:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SensitiveDataItemCategory value: {data!r}")
    return cast(SensitiveDataItemCategory, data)
