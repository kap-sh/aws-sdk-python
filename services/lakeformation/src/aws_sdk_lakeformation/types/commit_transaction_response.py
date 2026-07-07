"""Generated from Smithy shape ``com.amazonaws.lakeformation#CommitTransactionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.transaction_status


class CommitTransactionResponse(TypedDict, closed=True):
    transaction_status: NotRequired[
        "aws_sdk_lakeformation.types.transaction_status.TransactionStatus"
    ]
    """<p>The status of the transaction.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CommitTransactionResponse) -> dict:
    out: dict = {}
    if "transaction_status" in value:
        import aws_sdk_lakeformation.types.transaction_status

        out["TransactionStatus"] = (
            aws_sdk_lakeformation.types.transaction_status.serialize_json(
                value["transaction_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> CommitTransactionResponse:
    out: CommitTransactionResponse = {}  # type: ignore[typeddict-item]
    if "TransactionStatus" in data:
        import aws_sdk_lakeformation.types.transaction_status

        out["transaction_status"] = (
            aws_sdk_lakeformation.types.transaction_status.deserialize_json(
                data["TransactionStatus"]
            )
        )
    return out
