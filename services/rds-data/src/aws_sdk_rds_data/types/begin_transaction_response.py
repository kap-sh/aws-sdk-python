"""Generated from Smithy shape ``com.amazonaws.rdsdata#BeginTransactionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rds_data.types.id


class BeginTransactionResponse(TypedDict):
    transaction_id: NotRequired["aws_sdk_rds_data.types.id.Id"]
    """<p>The transaction ID of the transaction started by the call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BeginTransactionResponse) -> dict:
    out: dict = {}
    if "transaction_id" in value:
        out["transactionId"] = value["transaction_id"]
    return out


def deserialize_json(data: dict) -> BeginTransactionResponse:
    out: BeginTransactionResponse = {}  # type: ignore[typeddict-item]
    if "transactionId" in data:
        out["transaction_id"] = data["transactionId"]
    return out
