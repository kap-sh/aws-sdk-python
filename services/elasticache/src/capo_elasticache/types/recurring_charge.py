"""Generated from Smithy shape ``com.amazonaws.elasticache#RecurringCharge``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.double
    import capo_elasticache.types.string


class RecurringCharge(TypedDict, closed=True):
    recurring_charge_amount: NotRequired["capo_elasticache.types.double.Double"]
    """<p>The monetary amount of the recurring charge.</p>"""
    recurring_charge_frequency: NotRequired["capo_elasticache.types.string.String"]
    """<p>The frequency of the recurring charge.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RecurringCharge, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "recurring_charge_amount" in value:
        pairs.append(
            (
                f"{key_prefix}RecurringChargeAmount",
                str(value["recurring_charge_amount"]),
            )
        )
    if "recurring_charge_frequency" in value:
        pairs.append(
            (
                f"{key_prefix}RecurringChargeFrequency",
                str(value["recurring_charge_frequency"]),
            )
        )


def deserialize_query(el: Element) -> RecurringCharge:
    out: RecurringCharge = {}  # type: ignore[typeddict-item]
    child_recurring_charge_amount = el.find("RecurringChargeAmount")
    if child_recurring_charge_amount is not None:
        out["recurring_charge_amount"] = float(child_recurring_charge_amount.text or "")
    child_recurring_charge_frequency = el.find("RecurringChargeFrequency")
    if child_recurring_charge_frequency is not None:
        out["recurring_charge_frequency"] = str(
            child_recurring_charge_frequency.text or ""
        )
    return out
