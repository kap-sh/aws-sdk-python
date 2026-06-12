"""Generated from Smithy shape ``com.amazonaws.lakeformation#StartTransactionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.transaction_type


class StartTransactionRequest(TypedDict):
    transaction_type: NotRequired[
        "aws_sdk_lakeformation.types.transaction_type.TransactionType"
    ]
    """<p>Indicates whether this transaction should be read only or read and write. Writes made using a read-only transaction ID will be rejected. Read-only transactions do not need to be committed. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartTransactionRequest) -> dict:
    out: dict = {}
    if "transaction_type" in value:
        import aws_sdk_lakeformation.types.transaction_type

        out["TransactionType"] = (
            aws_sdk_lakeformation.types.transaction_type.serialize_json(
                value["transaction_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartTransactionRequest:
    out: StartTransactionRequest = {}  # type: ignore[typeddict-item]
    if "TransactionType" in data:
        import aws_sdk_lakeformation.types.transaction_type

        out["transaction_type"] = (
            aws_sdk_lakeformation.types.transaction_type.deserialize_json(
                data["TransactionType"]
            )
        )
    return out
