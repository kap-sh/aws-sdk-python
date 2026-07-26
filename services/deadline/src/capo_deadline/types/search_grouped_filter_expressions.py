"""Generated from Smithy shape ``com.amazonaws.deadline#SearchGroupedFilterExpressions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.logical_operator
    import capo_deadline.types.search_filter_expressions


class SearchGroupedFilterExpressions(TypedDict, closed=True):
    filters: "capo_deadline.types.search_filter_expressions.SearchFilterExpressions"
    """<p>The filters to use for the search.</p>"""
    operator: "capo_deadline.types.logical_operator.LogicalOperator"
    """<p>The operators to include in the search.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchGroupedFilterExpressions) -> dict:
    out: dict = {}
    import capo_deadline.types.search_filter_expressions

    out["filters"] = capo_deadline.types.search_filter_expressions.serialize_json(
        value["filters"]
    )
    import capo_deadline.types.logical_operator

    out["operator"] = capo_deadline.types.logical_operator.serialize_json(
        value["operator"]
    )
    return out


def deserialize_json(data: dict) -> SearchGroupedFilterExpressions:
    out: SearchGroupedFilterExpressions = {}  # type: ignore[typeddict-item]
    if "filters" in data:
        import capo_deadline.types.search_filter_expressions

        out["filters"] = capo_deadline.types.search_filter_expressions.deserialize_json(
            data["filters"]
        )
    else:
        raise DeserializationError("SearchGroupedFilterExpressions.filters required")
    if "operator" in data:
        import capo_deadline.types.logical_operator

        out["operator"] = capo_deadline.types.logical_operator.deserialize_json(
            data["operator"]
        )
    else:
        raise DeserializationError("SearchGroupedFilterExpressions.operator required")
    return out
