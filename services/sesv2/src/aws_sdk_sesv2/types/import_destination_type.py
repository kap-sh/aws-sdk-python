"""Generated from Smithy shape ``com.amazonaws.sesv2#ImportDestinationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sesv2.errors import DeserializationError

"""<p>The destination of the import job, which can be used to list import jobs that have a certain <code>ImportDestinationType</code>.</p>"""
ImportDestinationType: TypeAlias = Literal[
    "SUPPRESSION_LIST",
    "CONTACT_LIST",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUPPRESSION_LIST",
        "CONTACT_LIST",
    )
)


def serialize_json(value: ImportDestinationType) -> str:
    return value


def deserialize_json(data: str) -> ImportDestinationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImportDestinationType value: {data!r}")
    return cast(ImportDestinationType, data)
