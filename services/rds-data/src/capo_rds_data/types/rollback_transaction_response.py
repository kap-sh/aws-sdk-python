"""Generated from Smithy shape ``com.amazonaws.rdsdata#RollbackTransactionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rds_data.types.transaction_status


class RollbackTransactionResponse(TypedDict, closed=True):
    transaction_status: NotRequired[
        "capo_rds_data.types.transaction_status.TransactionStatus"
    ]
    """<p>The status of the rollback operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RollbackTransactionResponse) -> dict:
    out: dict = {}
    if "transaction_status" in value:
        out["transactionStatus"] = value["transaction_status"]
    return out


def deserialize_json(data: dict) -> RollbackTransactionResponse:
    out: RollbackTransactionResponse = {}  # type: ignore[typeddict-item]
    if "transactionStatus" in data:
        out["transaction_status"] = data["transactionStatus"]
    return out
