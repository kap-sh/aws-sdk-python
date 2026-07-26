"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetSessionActionIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.batch_get_session_action_identifier

BatchGetSessionActionIdentifiers: TypeAlias = list[
    "capo_deadline.types.batch_get_session_action_identifier.BatchGetSessionActionIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetSessionActionIdentifiers) -> list:
    import capo_deadline.types.batch_get_session_action_identifier

    out: list = []
    for item in value:
        out.append(
            capo_deadline.types.batch_get_session_action_identifier.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BatchGetSessionActionIdentifiers:
    import capo_deadline.types.batch_get_session_action_identifier

    out: BatchGetSessionActionIdentifiers = []
    for item in data:
        out.append(
            capo_deadline.types.batch_get_session_action_identifier.deserialize_json(
                item
            )
        )
    return out
