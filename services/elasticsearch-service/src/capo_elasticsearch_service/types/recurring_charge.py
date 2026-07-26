"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#RecurringCharge``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.double
    import capo_elasticsearch_service.types.string


class RecurringCharge(TypedDict, closed=True):
    recurring_charge_amount: NotRequired[
        "capo_elasticsearch_service.types.double.Double"
    ]
    """<p>The monetary amount of the recurring charge.</p>"""
    recurring_charge_frequency: NotRequired[
        "capo_elasticsearch_service.types.string.String"
    ]
    """<p>The frequency of the recurring charge.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecurringCharge) -> dict:
    out: dict = {}
    if "recurring_charge_amount" in value:
        out["RecurringChargeAmount"] = value["recurring_charge_amount"]
    if "recurring_charge_frequency" in value:
        out["RecurringChargeFrequency"] = value["recurring_charge_frequency"]
    return out


def deserialize_json(data: dict) -> RecurringCharge:
    out: RecurringCharge = {}  # type: ignore[typeddict-item]
    if "RecurringChargeAmount" in data:
        out["recurring_charge_amount"] = data["RecurringChargeAmount"]
    if "RecurringChargeFrequency" in data:
        out["recurring_charge_frequency"] = data["RecurringChargeFrequency"]
    return out
