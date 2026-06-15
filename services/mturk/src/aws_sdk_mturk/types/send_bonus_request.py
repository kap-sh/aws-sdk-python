"""Generated from Smithy shape ``com.amazonaws.mturk#SendBonusRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mturk.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mturk.types.currency_amount
    import aws_sdk_mturk.types.customer_id
    import aws_sdk_mturk.types.entity_id
    import aws_sdk_mturk.types.idempotency_token
    import aws_sdk_mturk.types.string


class SendBonusRequest(TypedDict):
    worker_id: "aws_sdk_mturk.types.customer_id.CustomerId"
    """<p>The ID of the Worker being paid the bonus.</p>"""
    bonus_amount: "aws_sdk_mturk.types.currency_amount.CurrencyAmount"
    r"""<p> The Bonus amount is a US Dollar amount specified using a string (for example, \"5\" represents $5.00 USD and \"101.42\" represents $101.42 USD). Do not include currency symbols or currency codes. </p>"""
    assignment_id: "aws_sdk_mturk.types.entity_id.EntityId"
    """<p>The ID of the assignment for which this bonus is paid.</p>"""
    reason: "aws_sdk_mturk.types.string.String"
    """<p>A message that explains the reason for the bonus payment. The Worker receiving the bonus can see this message.</p>"""
    unique_request_token: NotRequired[
        "aws_sdk_mturk.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique identifier for this request, which allows you to retry the call on error without granting multiple bonuses. This is useful in cases such as network timeouts where it is unclear whether or not the call succeeded on the server. If the bonus already exists in the system from a previous call using the same UniqueRequestToken, subsequent calls will return an error with a message containing the request ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SendBonusRequest) -> dict:
    out: dict = {}
    out["WorkerId"] = value["worker_id"]
    out["BonusAmount"] = value["bonus_amount"]
    out["AssignmentId"] = value["assignment_id"]
    out["Reason"] = value["reason"]
    if "unique_request_token" in value:
        out["UniqueRequestToken"] = value["unique_request_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SendBonusRequest:
    out: SendBonusRequest = {}  # type: ignore[typeddict-item]
    if "WorkerId" in data:
        out["worker_id"] = data["WorkerId"]
    else:
        raise DeserializationError("SendBonusRequest.worker_id required")
    if "BonusAmount" in data:
        out["bonus_amount"] = data["BonusAmount"]
    else:
        raise DeserializationError("SendBonusRequest.bonus_amount required")
    if "AssignmentId" in data:
        out["assignment_id"] = data["AssignmentId"]
    else:
        raise DeserializationError("SendBonusRequest.assignment_id required")
    if "Reason" in data:
        out["reason"] = data["Reason"]
    else:
        raise DeserializationError("SendBonusRequest.reason required")
    if "UniqueRequestToken" in data:
        out["unique_request_token"] = data["UniqueRequestToken"]
    return out
