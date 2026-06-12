"""Generated from Smithy shape ``com.amazonaws.rds#RecurringCharge``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.double
    import aws_sdk_rds.types.string


class RecurringCharge(TypedDict):
    recurring_charge_amount: NotRequired["aws_sdk_rds.types.double.Double"]
    """<p>The amount of the recurring charge.</p>"""
    recurring_charge_frequency: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The frequency of the recurring charge.</p>"""


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
