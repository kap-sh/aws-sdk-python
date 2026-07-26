"""Generated from Smithy shape ``com.amazonaws.rtbfabric#FilterCriterion``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rtbfabric.types.value_list


class FilterCriterion(TypedDict, closed=True):
    path: "str"
    """<p>The path to filter.</p>"""
    values: "capo_rtbfabric.types.value_list.ValueList"
    """<p>The value to filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterCriterion) -> dict:
    out: dict = {}
    out["path"] = value["path"]
    import capo_rtbfabric.types.value_list

    out["values"] = capo_rtbfabric.types.value_list.serialize_json(value["values"])
    return out


def deserialize_json(data: dict) -> FilterCriterion:
    out: FilterCriterion = {}  # type: ignore[typeddict-item]
    if "path" in data:
        out["path"] = data["path"]
    else:
        raise DeserializationError("FilterCriterion.path required")
    if "values" in data:
        import capo_rtbfabric.types.value_list

        out["values"] = capo_rtbfabric.types.value_list.deserialize_json(data["values"])
    else:
        raise DeserializationError("FilterCriterion.values required")
    return out
