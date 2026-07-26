"""Generated from Smithy shape ``com.amazonaws.cleanrooms#QueryConstraint``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.query_constraint_require_overlap


class _QueryConstraint_requireOverlap(TypedDict, closed=True):
    requireOverlap: "capo_cleanrooms.types.query_constraint_require_overlap.QueryConstraintRequireOverlap"


QueryConstraint: TypeAlias = _QueryConstraint_requireOverlap


# --- restJson1 ser/de ---
def serialize_json(value: QueryConstraint) -> dict:
    if "requireOverlap" in value:
        import capo_cleanrooms.types.query_constraint_require_overlap

        return {
            "requireOverlap": capo_cleanrooms.types.query_constraint_require_overlap.serialize_json(
                value["requireOverlap"]
            )
        }
    else:
        raise SerializationError("QueryConstraint: no variant present")


def deserialize_json(data: dict) -> QueryConstraint:
    if "requireOverlap" in data:
        import capo_cleanrooms.types.query_constraint_require_overlap

        return {
            "requireOverlap": capo_cleanrooms.types.query_constraint_require_overlap.deserialize_json(
                data["requireOverlap"]
            )
        }
    else:
        raise DeserializationError("QueryConstraint: no recognized variant key")
