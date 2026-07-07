"""Generated from Smithy shape ``com.amazonaws.devicefarm#RecurringCharge``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.monetary_amount
    import aws_sdk_device_farm.types.recurring_charge_frequency


class RecurringCharge(TypedDict, closed=True):
    cost: NotRequired["aws_sdk_device_farm.types.monetary_amount.MonetaryAmount"]
    """<p>The cost of the recurring charge.</p>"""
    frequency: NotRequired[
        "aws_sdk_device_farm.types.recurring_charge_frequency.RecurringChargeFrequency"
    ]
    """<p>The frequency in which charges recur.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecurringCharge) -> dict:
    out: dict = {}
    if "cost" in value:
        import aws_sdk_device_farm.types.monetary_amount

        out["cost"] = aws_sdk_device_farm.types.monetary_amount.serialize_aws_json_1_1(
            value["cost"]
        )
    if "frequency" in value:
        import aws_sdk_device_farm.types.recurring_charge_frequency

        out["frequency"] = (
            aws_sdk_device_farm.types.recurring_charge_frequency.serialize_aws_json_1_1(
                value["frequency"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RecurringCharge:
    out: RecurringCharge = {}  # type: ignore[typeddict-item]
    if "cost" in data:
        import aws_sdk_device_farm.types.monetary_amount

        out["cost"] = (
            aws_sdk_device_farm.types.monetary_amount.deserialize_aws_json_1_1(
                data["cost"]
            )
        )
    if "frequency" in data:
        import aws_sdk_device_farm.types.recurring_charge_frequency

        out["frequency"] = (
            aws_sdk_device_farm.types.recurring_charge_frequency.deserialize_aws_json_1_1(
                data["frequency"]
            )
        )
    return out
