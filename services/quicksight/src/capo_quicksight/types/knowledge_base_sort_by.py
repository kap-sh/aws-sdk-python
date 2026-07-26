"""Generated from Smithy shape ``com.amazonaws.quicksight#KnowledgeBaseSortBy``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.knowledge_base_sort_by_field
    import capo_quicksight.types.sort_order


class KnowledgeBaseSortBy(TypedDict, closed=True):
    sort_by_field: (
        "capo_quicksight.types.knowledge_base_sort_by_field.KnowledgeBaseSortByField"
    )
    """<p>The field to sort by.</p>"""
    sort_order: "capo_quicksight.types.sort_order.SortOrder"
    """<p>The sort order (ascending or descending).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseSortBy) -> dict:
    out: dict = {}
    import capo_quicksight.types.knowledge_base_sort_by_field

    out["sortByField"] = (
        capo_quicksight.types.knowledge_base_sort_by_field.serialize_json(
            value["sort_by_field"]
        )
    )
    import capo_quicksight.types.sort_order

    out["sortOrder"] = capo_quicksight.types.sort_order.serialize_json(
        value["sort_order"]
    )
    return out


def deserialize_json(data: dict) -> KnowledgeBaseSortBy:
    out: KnowledgeBaseSortBy = {}  # type: ignore[typeddict-item]
    if "sortByField" in data:
        import capo_quicksight.types.knowledge_base_sort_by_field

        out["sort_by_field"] = (
            capo_quicksight.types.knowledge_base_sort_by_field.deserialize_json(
                data["sortByField"]
            )
        )
    else:
        raise DeserializationError("KnowledgeBaseSortBy.sort_by_field required")
    if "sortOrder" in data:
        import capo_quicksight.types.sort_order

        out["sort_order"] = capo_quicksight.types.sort_order.deserialize_json(
            data["sortOrder"]
        )
    else:
        raise DeserializationError("KnowledgeBaseSortBy.sort_order required")
    return out
