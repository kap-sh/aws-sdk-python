"""Generated from Smithy shape ``com.amazonaws.wisdom#SearchExpression``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_wisdom.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wisdom.types.filter_list


class SearchExpression(TypedDict, closed=True):
    filters: "capo_wisdom.types.filter_list.FilterList"
    """<p>The search expression filters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchExpression) -> dict:
    out: dict = {}
    import capo_wisdom.types.filter_list

    out["filters"] = capo_wisdom.types.filter_list.serialize_json(value["filters"])
    return out


def deserialize_json(data: dict) -> SearchExpression:
    out: SearchExpression = {}  # type: ignore[typeddict-item]
    if "filters" in data:
        import capo_wisdom.types.filter_list

        out["filters"] = capo_wisdom.types.filter_list.deserialize_json(data["filters"])
    else:
        raise DeserializationError("SearchExpression.filters required")
    return out
