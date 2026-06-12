"""Generated from Smithy shape ``com.amazonaws.mturk#BonusPayment``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mturk.types.currency_amount
    import aws_sdk_mturk.types.customer_id
    import aws_sdk_mturk.types.entity_id
    import aws_sdk_mturk.types.string
    import aws_sdk_mturk.types.timestamp


class BonusPayment(TypedDict):
    worker_id: NotRequired["aws_sdk_mturk.types.customer_id.CustomerId"]
    """<p>The ID of the Worker to whom the bonus was paid.</p>"""
    bonus_amount: NotRequired["aws_sdk_mturk.types.currency_amount.CurrencyAmount"]
    assignment_id: NotRequired["aws_sdk_mturk.types.entity_id.EntityId"]
    """<p>The ID of the assignment associated with this bonus payment.</p>"""
    reason: NotRequired["aws_sdk_mturk.types.string.String"]
    """<p>The Reason text given when the bonus was granted, if any.</p>"""
    grant_time: NotRequired["aws_sdk_mturk.types.timestamp.Timestamp"]
    """<p>The date and time of when the bonus was granted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BonusPayment) -> dict:
    out: dict = {}
    if "worker_id" in value:
        out["WorkerId"] = value["worker_id"]
    if "bonus_amount" in value:
        out["BonusAmount"] = value["bonus_amount"]
    if "assignment_id" in value:
        out["AssignmentId"] = value["assignment_id"]
    if "reason" in value:
        out["Reason"] = value["reason"]
    if "grant_time" in value:
        import aws_sdk_mturk.types.timestamp

        out["GrantTime"] = aws_sdk_mturk.types.timestamp.serialize_aws_json_1_1(
            value["grant_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BonusPayment:
    out: BonusPayment = {}  # type: ignore[typeddict-item]
    if "WorkerId" in data:
        out["worker_id"] = data["WorkerId"]
    if "BonusAmount" in data:
        out["bonus_amount"] = data["BonusAmount"]
    if "AssignmentId" in data:
        out["assignment_id"] = data["AssignmentId"]
    if "Reason" in data:
        out["reason"] = data["Reason"]
    if "GrantTime" in data:
        import aws_sdk_mturk.types.timestamp

        out["grant_time"] = aws_sdk_mturk.types.timestamp.deserialize_aws_json_1_1(
            data["GrantTime"]
        )
    return out
