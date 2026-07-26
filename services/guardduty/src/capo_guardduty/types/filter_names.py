"""Generated from Smithy shape ``com.amazonaws.guardduty#FilterNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.filter_name

FilterNames: TypeAlias = list["capo_guardduty.types.filter_name.FilterName"]


# --- restJson1 ser/de ---
def serialize_json(value: FilterNames) -> list:
    return list(value)


def deserialize_json(data: list) -> FilterNames:
    return list(data)
