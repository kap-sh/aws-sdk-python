"""Generated from Smithy shape ``com.amazonaws.redshift#RecurringCharge``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.double
    import aws_sdk_redshift.types.string


class RecurringCharge(TypedDict, closed=True):
    recurring_charge_amount: NotRequired["aws_sdk_redshift.types.double.Double"]
    """<p>The amount charged per the period of time specified by the recurring charge frequency.</p>"""
    recurring_charge_frequency: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The frequency at which the recurring charge amount is applied.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RecurringCharge, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "recurring_charge_amount" in value:
        pairs.append(
            (f"{prefix}.RecurringChargeAmount", str(value["recurring_charge_amount"]))
        )
    if "recurring_charge_frequency" in value:
        pairs.append(
            (
                f"{prefix}.RecurringChargeFrequency",
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
