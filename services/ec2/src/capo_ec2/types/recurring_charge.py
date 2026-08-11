"""Generated from Smithy shape ``com.amazonaws.ec2#RecurringCharge``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.double
    import capo_ec2.types.recurring_charge_frequency


class RecurringCharge(TypedDict, closed=True):
    amount: NotRequired["capo_ec2.types.double.Double"]
    """<p>The amount of the recurring charge.</p>"""
    frequency: NotRequired[
        "capo_ec2.types.recurring_charge_frequency.RecurringChargeFrequency"
    ]
    """<p>The frequency of the recurring charge.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RecurringCharge, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "amount" in value:
        pairs.append(
            (
                f"{key_prefix}Amount",
                (
                    "NaN"
                    if value["amount"] != value["amount"]
                    else "Infinity"
                    if value["amount"] == float("inf")
                    else "-Infinity"
                    if value["amount"] == float("-inf")
                    else str(value["amount"])
                ),
            )
        )
    if "frequency" in value:
        import capo_ec2.types.recurring_charge_frequency

        capo_ec2.types.recurring_charge_frequency.serialize_ec2_query(
            value["frequency"], pairs, f"{key_prefix}Frequency"
        )


def deserialize_ec2_query(el: Element) -> RecurringCharge:
    out: RecurringCharge = {}  # type: ignore[typeddict-item]
    child_amount = el.find("amount")
    if child_amount is not None:
        out["amount"] = float(child_amount.text or "")
    child_frequency = el.find("frequency")
    if child_frequency is not None:
        import capo_ec2.types.recurring_charge_frequency

        out["frequency"] = (
            capo_ec2.types.recurring_charge_frequency.deserialize_ec2_query(
                child_frequency
            )
        )
    return out
