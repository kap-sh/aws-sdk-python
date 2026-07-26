"""Generated from Smithy shape ``com.amazonaws.inspector2#StringFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector2.types.string_comparison
    import capo_inspector2.types.string_input


class StringFilter(TypedDict, closed=True):
    comparison: "capo_inspector2.types.string_comparison.StringComparison"
    """<p>The operator to use when comparing values in the filter.</p>"""
    value: "capo_inspector2.types.string_input.StringInput"
    """<p>The value to filter on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StringFilter) -> dict:
    out: dict = {}
    out["comparison"] = value["comparison"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> StringFilter:
    out: StringFilter = {}  # type: ignore[typeddict-item]
    if "comparison" in data:
        out["comparison"] = data["comparison"]
    else:
        raise DeserializationError("StringFilter.comparison required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("StringFilter.value required")
    return out
