"""Generated from Smithy shape ``com.amazonaws.cleanrooms#QueryConstraintList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.query_constraint

QueryConstraintList: TypeAlias = list[
    "aws_sdk_cleanrooms.types.query_constraint.QueryConstraint"
]


# --- restJson1 ser/de ---
def serialize_json(value: QueryConstraintList) -> list:
    import aws_sdk_cleanrooms.types.query_constraint

    out: list = []
    for item in value:
        out.append(aws_sdk_cleanrooms.types.query_constraint.serialize_json(item))
    return out


def deserialize_json(data: list) -> QueryConstraintList:
    import aws_sdk_cleanrooms.types.query_constraint

    out: QueryConstraintList = []
    for item in data:
        out.append(aws_sdk_cleanrooms.types.query_constraint.deserialize_json(item))
    return out
