"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetSessionIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.batch_get_session_identifier

BatchGetSessionIdentifiers: TypeAlias = list[
    "capo_deadline.types.batch_get_session_identifier.BatchGetSessionIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetSessionIdentifiers) -> list:
    import capo_deadline.types.batch_get_session_identifier

    out: list = []
    for item in value:
        out.append(
            capo_deadline.types.batch_get_session_identifier.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BatchGetSessionIdentifiers:
    import capo_deadline.types.batch_get_session_identifier

    out: BatchGetSessionIdentifiers = []
    for item in data:
        out.append(
            capo_deadline.types.batch_get_session_identifier.deserialize_json(item)
        )
    return out
