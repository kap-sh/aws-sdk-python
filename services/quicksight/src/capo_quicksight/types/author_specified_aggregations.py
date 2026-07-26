"""Generated from Smithy shape ``com.amazonaws.quicksight#AuthorSpecifiedAggregations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.author_specified_aggregation

AuthorSpecifiedAggregations: TypeAlias = list[
    "capo_quicksight.types.author_specified_aggregation.AuthorSpecifiedAggregation"
]


# --- restJson1 ser/de ---
def serialize_json(value: AuthorSpecifiedAggregations) -> list:
    import capo_quicksight.types.author_specified_aggregation

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.author_specified_aggregation.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AuthorSpecifiedAggregations:
    import capo_quicksight.types.author_specified_aggregation

    out: AuthorSpecifiedAggregations = []
    for item in data:
        out.append(
            capo_quicksight.types.author_specified_aggregation.deserialize_json(item)
        )
    return out
