"""Generated from Smithy shape ``com.amazonaws.qbusiness#BlockedPhrases``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qbusiness.types.blocked_phrase

BlockedPhrases: TypeAlias = list["capo_qbusiness.types.blocked_phrase.BlockedPhrase"]


# --- restJson1 ser/de ---
def serialize_json(value: BlockedPhrases) -> list:
    return list(value)


def deserialize_json(data: list) -> BlockedPhrases:
    return list(data)
