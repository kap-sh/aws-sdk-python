"""Generated from Smithy shape ``com.amazonaws.rdsdata#CommitTransactionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rds_data.types.transaction_status


class CommitTransactionResponse(TypedDict, closed=True):
    transaction_status: NotRequired[
        "capo_rds_data.types.transaction_status.TransactionStatus"
    ]
    """<p>The status of the commit operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CommitTransactionResponse) -> dict:
    out: dict = {}
    if "transaction_status" in value:
        out["transactionStatus"] = value["transaction_status"]
    return out


def deserialize_json(data: dict) -> CommitTransactionResponse:
    out: CommitTransactionResponse = {}  # type: ignore[typeddict-item]
    if "transactionStatus" in data:
        out["transaction_status"] = data["transactionStatus"]
    return out
