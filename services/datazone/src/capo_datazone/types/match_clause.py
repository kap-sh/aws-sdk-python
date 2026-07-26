"""Generated from Smithy shape ``com.amazonaws.datazone#MatchClause``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_datazone.types.entity_pattern
    import capo_datazone.types.relation_pattern


class _MatchClause_relationPattern(TypedDict, closed=True):
    relationPattern: "capo_datazone.types.relation_pattern.RelationPattern"


class _MatchClause_entityPattern(TypedDict, closed=True):
    entityPattern: "capo_datazone.types.entity_pattern.EntityPattern"


MatchClause: TypeAlias = _MatchClause_relationPattern | _MatchClause_entityPattern


# --- restJson1 ser/de ---
def serialize_json(value: MatchClause) -> dict:
    if "relationPattern" in value:
        import capo_datazone.types.relation_pattern

        return {
            "relationPattern": capo_datazone.types.relation_pattern.serialize_json(
                value["relationPattern"]
            )
        }
    elif "entityPattern" in value:
        import capo_datazone.types.entity_pattern

        return {
            "entityPattern": capo_datazone.types.entity_pattern.serialize_json(
                value["entityPattern"]
            )
        }
    else:
        raise SerializationError("MatchClause: no variant present")


def deserialize_json(data: dict) -> MatchClause:
    if "relationPattern" in data:
        import capo_datazone.types.relation_pattern

        return {
            "relationPattern": capo_datazone.types.relation_pattern.deserialize_json(
                data["relationPattern"]
            )
        }
    elif "entityPattern" in data:
        import capo_datazone.types.entity_pattern

        return {
            "entityPattern": capo_datazone.types.entity_pattern.deserialize_json(
                data["entityPattern"]
            )
        }
    else:
        raise DeserializationError("MatchClause: no recognized variant key")
