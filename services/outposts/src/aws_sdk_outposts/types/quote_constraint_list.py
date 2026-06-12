"""Generated from Smithy shape ``com.amazonaws.outposts#QuoteConstraintList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_outposts.types.quote_constraint

QuoteConstraintList: TypeAlias = list[
    "aws_sdk_outposts.types.quote_constraint.QuoteConstraint"
]


# --- restJson1 ser/de ---
def serialize_json(value: QuoteConstraintList) -> list:
    import aws_sdk_outposts.types.quote_constraint

    out: list = []
    for item in value:
        out.append(aws_sdk_outposts.types.quote_constraint.serialize_json(item))
    return out


def deserialize_json(data: list) -> QuoteConstraintList:
    import aws_sdk_outposts.types.quote_constraint

    out: QuoteConstraintList = []
    for item in data:
        out.append(aws_sdk_outposts.types.quote_constraint.deserialize_json(item))
    return out
