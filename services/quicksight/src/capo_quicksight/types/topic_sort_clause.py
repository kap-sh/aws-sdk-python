"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicSortClause``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.identifier
    import capo_quicksight.types.topic_sort_direction


class TopicSortClause(TypedDict, closed=True):
    operand: NotRequired["capo_quicksight.types.identifier.Identifier"]
    """<p>The operand for a <code>TopicSortClause</code>.</p>"""
    sort_direction: NotRequired[
        "capo_quicksight.types.topic_sort_direction.TopicSortDirection"
    ]
    """<p>The sort direction for the <code>TopicSortClause</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicSortClause) -> dict:
    out: dict = {}
    if "operand" in value:
        import capo_quicksight.types.identifier

        out["Operand"] = capo_quicksight.types.identifier.serialize_json(
            value["operand"]
        )
    if "sort_direction" in value:
        import capo_quicksight.types.topic_sort_direction

        out["SortDirection"] = (
            capo_quicksight.types.topic_sort_direction.serialize_json(
                value["sort_direction"]
            )
        )
    return out


def deserialize_json(data: dict) -> TopicSortClause:
    out: TopicSortClause = {}  # type: ignore[typeddict-item]
    if "Operand" in data:
        import capo_quicksight.types.identifier

        out["operand"] = capo_quicksight.types.identifier.deserialize_json(
            data["Operand"]
        )
    if "SortDirection" in data:
        import capo_quicksight.types.topic_sort_direction

        out["sort_direction"] = (
            capo_quicksight.types.topic_sort_direction.deserialize_json(
                data["SortDirection"]
            )
        )
    return out
