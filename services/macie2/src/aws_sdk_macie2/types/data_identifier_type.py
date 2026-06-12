"""Generated from Smithy shape ``com.amazonaws.macie2#DataIdentifierType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

"""<p>The type of data identifier that detected a specific type of sensitive data in an S3 bucket. Possible values are:</p>"""
DataIdentifierType: TypeAlias = Literal[
    "CUSTOM",
    "MANAGED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CUSTOM",
        "MANAGED",
    )
)


def serialize_json(value: DataIdentifierType) -> str:
    return value


def deserialize_json(data: str) -> DataIdentifierType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataIdentifierType value: {data!r}")
    return cast(DataIdentifierType, data)
