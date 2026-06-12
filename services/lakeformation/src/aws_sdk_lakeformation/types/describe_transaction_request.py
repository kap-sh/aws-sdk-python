"""Generated from Smithy shape ``com.amazonaws.lakeformation#DescribeTransactionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.transaction_id_string


class DescribeTransactionRequest(TypedDict):
    transaction_id: (
        "aws_sdk_lakeformation.types.transaction_id_string.TransactionIdString"
    )
    """<p>The transaction for which to return status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeTransactionRequest) -> dict:
    out: dict = {}
    out["TransactionId"] = value["transaction_id"]
    return out


def deserialize_json(data: dict) -> DescribeTransactionRequest:
    out: DescribeTransactionRequest = {}  # type: ignore[typeddict-item]
    if "TransactionId" in data:
        out["transaction_id"] = data["TransactionId"]
    else:
        raise DeserializationError("DescribeTransactionRequest.transaction_id required")
    return out
