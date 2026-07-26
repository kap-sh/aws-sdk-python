"""Generated from Smithy shape ``com.amazonaws.cleanrooms#QueryConstraintList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.query_constraint

QueryConstraintList: TypeAlias = list[
    "capo_cleanrooms.types.query_constraint.QueryConstraint"
]


# --- restJson1 ser/de ---
def serialize_json(value: QueryConstraintList) -> list:
    import capo_cleanrooms.types.query_constraint

    out: list = []
    for item in value:
        out.append(capo_cleanrooms.types.query_constraint.serialize_json(item))
    return out


def deserialize_json(data: list) -> QueryConstraintList:
    import capo_cleanrooms.types.query_constraint

    out: QueryConstraintList = []
    for item in data:
        out.append(capo_cleanrooms.types.query_constraint.deserialize_json(item))
    return out
