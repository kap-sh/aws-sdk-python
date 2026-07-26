"""Generated from Smithy shape ``com.amazonaws.wisdom#Filter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_wisdom.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wisdom.types.filter_field
    import capo_wisdom.types.filter_operator
    import capo_wisdom.types.non_empty_string


class Filter(TypedDict, closed=True):
    field: "capo_wisdom.types.filter_field.FilterField"
    """<p>The field on which to filter.</p>"""
    operator: "capo_wisdom.types.filter_operator.FilterOperator"
    """<p>The operator to use for comparing the field’s value with the provided value.</p>"""
    value: "capo_wisdom.types.non_empty_string.NonEmptyString"
    """<p>The desired field value on which to filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Filter) -> dict:
    out: dict = {}
    out["field"] = value["field"]
    out["operator"] = value["operator"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if "field" in data:
        out["field"] = data["field"]
    else:
        raise DeserializationError("Filter.field required")
    if "operator" in data:
        out["operator"] = data["operator"]
    else:
        raise DeserializationError("Filter.operator required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("Filter.value required")
    return out
