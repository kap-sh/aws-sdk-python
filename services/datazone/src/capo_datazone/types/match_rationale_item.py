"""Generated from Smithy shape ``com.amazonaws.datazone#MatchRationaleItem``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_datazone.types.text_matches


class _MatchRationaleItem_textMatches(TypedDict, closed=True):
    textMatches: "capo_datazone.types.text_matches.TextMatches"


MatchRationaleItem: TypeAlias = _MatchRationaleItem_textMatches


# --- restJson1 ser/de ---
def serialize_json(value: MatchRationaleItem) -> dict:
    if "textMatches" in value:
        import capo_datazone.types.text_matches

        return {
            "textMatches": capo_datazone.types.text_matches.serialize_json(
                value["textMatches"]
            )
        }
    else:
        raise SerializationError("MatchRationaleItem: no variant present")


def deserialize_json(data: dict) -> MatchRationaleItem:
    if "textMatches" in data:
        import capo_datazone.types.text_matches

        return {
            "textMatches": capo_datazone.types.text_matches.deserialize_json(
                data["textMatches"]
            )
        }
    else:
        raise DeserializationError("MatchRationaleItem: no recognized variant key")
