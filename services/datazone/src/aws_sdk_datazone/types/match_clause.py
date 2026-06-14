"""Generated from Smithy shape ``com.amazonaws.datazone#MatchClause``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.entity_pattern
    import aws_sdk_datazone.types.relation_pattern


class _MatchClause_relationPattern(TypedDict):
    relationPattern: "aws_sdk_datazone.types.relation_pattern.RelationPattern"


class _MatchClause_entityPattern(TypedDict):
    entityPattern: "aws_sdk_datazone.types.entity_pattern.EntityPattern"


MatchClause: TypeAlias = _MatchClause_relationPattern | _MatchClause_entityPattern


# --- restJson1 ser/de ---
def serialize_json(value: MatchClause) -> dict:
    if "relationPattern" in value:
        import aws_sdk_datazone.types.relation_pattern

        return {
            "relationPattern": aws_sdk_datazone.types.relation_pattern.serialize_json(
                value["relationPattern"]
            )
        }
    elif "entityPattern" in value:
        import aws_sdk_datazone.types.entity_pattern

        return {
            "entityPattern": aws_sdk_datazone.types.entity_pattern.serialize_json(
                value["entityPattern"]
            )
        }
    else:
        raise SerializationError("MatchClause: no variant present")


def deserialize_json(data: dict) -> MatchClause:
    if "relationPattern" in data:
        import aws_sdk_datazone.types.relation_pattern

        return {
            "relationPattern": aws_sdk_datazone.types.relation_pattern.deserialize_json(
                data["relationPattern"]
            )
        }
    elif "entityPattern" in data:
        import aws_sdk_datazone.types.entity_pattern

        return {
            "entityPattern": aws_sdk_datazone.types.entity_pattern.deserialize_json(
                data["entityPattern"]
            )
        }
    else:
        raise DeserializationError("MatchClause: no recognized variant key")
