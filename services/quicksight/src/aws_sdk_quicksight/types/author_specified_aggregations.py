"""Generated from Smithy shape ``com.amazonaws.quicksight#AuthorSpecifiedAggregations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.author_specified_aggregation

AuthorSpecifiedAggregations: TypeAlias = list[
    "aws_sdk_quicksight.types.author_specified_aggregation.AuthorSpecifiedAggregation"
]


# --- restJson1 ser/de ---
def serialize_json(value: AuthorSpecifiedAggregations) -> list:
    import aws_sdk_quicksight.types.author_specified_aggregation

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.author_specified_aggregation.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AuthorSpecifiedAggregations:
    import aws_sdk_quicksight.types.author_specified_aggregation

    out: AuthorSpecifiedAggregations = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.author_specified_aggregation.deserialize_json(item)
        )
    return out
