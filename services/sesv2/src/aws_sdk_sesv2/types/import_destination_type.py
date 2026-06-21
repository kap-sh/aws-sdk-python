"""Generated from Smithy shape ``com.amazonaws.sesv2#ImportDestinationType``."""

from typing import Literal, TypeAlias, cast

"""<p>The destination of the import job, which can be used to list import jobs that have a certain <code>ImportDestinationType</code>.</p>"""
ImportDestinationType: TypeAlias = Literal[
    "SUPPRESSION_LIST",
    "CONTACT_LIST",
]


# --- restJson1 ser/de ---
def serialize_json(value: ImportDestinationType) -> str:
    return value


def deserialize_json(data: str) -> ImportDestinationType:
    return cast(ImportDestinationType, data)
