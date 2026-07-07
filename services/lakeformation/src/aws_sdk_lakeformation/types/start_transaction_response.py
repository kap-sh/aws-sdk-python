"""Generated from Smithy shape ``com.amazonaws.lakeformation#StartTransactionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.transaction_id_string


class StartTransactionResponse(TypedDict, closed=True):
    transaction_id: NotRequired[
        "aws_sdk_lakeformation.types.transaction_id_string.TransactionIdString"
    ]
    """<p>An opaque identifier for the transaction.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartTransactionResponse) -> dict:
    out: dict = {}
    if "transaction_id" in value:
        out["TransactionId"] = value["transaction_id"]
    return out


def deserialize_json(data: dict) -> StartTransactionResponse:
    out: StartTransactionResponse = {}  # type: ignore[typeddict-item]
    if "TransactionId" in data:
        out["transaction_id"] = data["TransactionId"]
    return out
