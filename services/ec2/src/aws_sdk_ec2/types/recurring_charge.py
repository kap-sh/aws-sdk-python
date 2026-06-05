"""Generated from Smithy shape ``com.amazonaws.ec2#RecurringCharge``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.double
    import aws_sdk_ec2.types.recurring_charge_frequency


class RecurringCharge(TypedDict):
    amount: NotRequired["aws_sdk_ec2.types.double.Double"]
    """<p>The amount of the recurring charge.</p>"""
    frequency: NotRequired[
        "aws_sdk_ec2.types.recurring_charge_frequency.RecurringChargeFrequency"
    ]
    """<p>The frequency of the recurring charge.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RecurringCharge, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "amount" in value:
        pairs.append((f"{prefix}.Amount", str(value["amount"])))
    if "frequency" in value:
        import aws_sdk_ec2.types.recurring_charge_frequency

        aws_sdk_ec2.types.recurring_charge_frequency.serialize_ec2_query(
            value["frequency"], pairs, f"{prefix}.Frequency"
        )


def deserialize_ec2_query(el: Element) -> RecurringCharge:
    out: RecurringCharge = {}  # type: ignore[typeddict-item]
    child_amount = el.find("Amount")
    if child_amount is not None:
        out["amount"] = float(child_amount.text or "")
    child_frequency = el.find("Frequency")
    if child_frequency is not None:
        import aws_sdk_ec2.types.recurring_charge_frequency

        out["frequency"] = (
            aws_sdk_ec2.types.recurring_charge_frequency.deserialize_ec2_query(
                child_frequency
            )
        )
    return out
