"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#ScheduleItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.bounded_string
    import aws_sdk_marketplace_agreement.types.timestamp


class ScheduleItem(TypedDict):
    charge_date: NotRequired["aws_sdk_marketplace_agreement.types.timestamp.Timestamp"]
    """<p>The date that the customer would pay the price defined in this payment schedule term. Invoices are generated on the date provided.</p>"""
    charge_amount: NotRequired[
        "aws_sdk_marketplace_agreement.types.bounded_string.BoundedString"
    ]
    """<p>The price that the customer would pay on the scheduled date (chargeDate).</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ScheduleItem) -> dict:
    out: dict = {}
    if "charge_date" in value:
        import aws_sdk_marketplace_agreement.types.timestamp

        out["chargeDate"] = (
            aws_sdk_marketplace_agreement.types.timestamp.serialize_aws_json_1_0(
                value["charge_date"]
            )
        )
    if "charge_amount" in value:
        out["chargeAmount"] = value["charge_amount"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ScheduleItem:
    out: ScheduleItem = {}  # type: ignore[typeddict-item]
    if "chargeDate" in data:
        import aws_sdk_marketplace_agreement.types.timestamp

        out["charge_date"] = (
            aws_sdk_marketplace_agreement.types.timestamp.deserialize_aws_json_1_0(
                data["chargeDate"]
            )
        )
    if "chargeAmount" in data:
        out["charge_amount"] = data["chargeAmount"]
    return out
