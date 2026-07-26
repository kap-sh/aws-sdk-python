"""Generated from Smithy shape ``com.amazonaws.braket#SearchSpendingLimitsFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_braket.errors import DeserializationError

if TYPE_CHECKING:
    import capo_braket.types.search_spending_limits_filter_operator
    import capo_braket.types.string64
    import capo_braket.types.string256_list


class SearchSpendingLimitsFilter(TypedDict, closed=True):
    name: "capo_braket.types.string64.String64"
    """<p>The name of the field to filter on. Currently only supports <code>deviceArn</code>.</p>"""
    values: "capo_braket.types.string256_list.String256List"
    """<p>An array of values to match against the specified field.</p>"""
    operator: "capo_braket.types.search_spending_limits_filter_operator.SearchSpendingLimitsFilterOperator"
    """<p>The comparison operator to use when filtering.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchSpendingLimitsFilter) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_braket.types.string256_list

    out["values"] = capo_braket.types.string256_list.serialize_json(value["values"])
    out["operator"] = value["operator"]
    return out


def deserialize_json(data: dict) -> SearchSpendingLimitsFilter:
    out: SearchSpendingLimitsFilter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("SearchSpendingLimitsFilter.name required")
    if "values" in data:
        import capo_braket.types.string256_list

        out["values"] = capo_braket.types.string256_list.deserialize_json(
            data["values"]
        )
    else:
        raise DeserializationError("SearchSpendingLimitsFilter.values required")
    if "operator" in data:
        out["operator"] = data["operator"]
    else:
        raise DeserializationError("SearchSpendingLimitsFilter.operator required")
    return out
