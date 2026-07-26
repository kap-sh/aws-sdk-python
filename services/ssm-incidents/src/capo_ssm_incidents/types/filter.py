"""Generated from Smithy shape ``com.amazonaws.ssmincidents#Filter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm_incidents.types.condition


class Filter(TypedDict, closed=True):
    key: "str"
    """<p>The key that you're filtering on.</p>"""
    condition: "capo_ssm_incidents.types.condition.Condition"
    """<p>The condition accepts before or after a specified time, equal to a string, or equal to an integer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Filter) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    import capo_ssm_incidents.types.condition

    out["condition"] = capo_ssm_incidents.types.condition.serialize_json(
        value["condition"]
    )
    return out


def deserialize_json(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("Filter.key required")
    if "condition" in data:
        import capo_ssm_incidents.types.condition

        out["condition"] = capo_ssm_incidents.types.condition.deserialize_json(
            data["condition"]
        )
    else:
        raise DeserializationError("Filter.condition required")
    return out
