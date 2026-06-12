"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanOfferingRateProperty``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_savingsplans.types.json_safe_filter_value_string


class SavingsPlanOfferingRateProperty(TypedDict):
    name: NotRequired[
        "aws_sdk_savingsplans.types.json_safe_filter_value_string.JsonSafeFilterValueString"
    ]
    """<p>The property name.</p>"""
    value: NotRequired[
        "aws_sdk_savingsplans.types.json_safe_filter_value_string.JsonSafeFilterValueString"
    ]
    """<p>The property value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SavingsPlanOfferingRateProperty) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> SavingsPlanOfferingRateProperty:
    out: SavingsPlanOfferingRateProperty = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "value" in data:
        out["value"] = data["value"]
    return out
