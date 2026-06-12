"""Generated from Smithy shape ``com.amazonaws.lakeformation#DescribeTransactionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.transaction_description


class DescribeTransactionResponse(TypedDict):
    transaction_description: NotRequired[
        "aws_sdk_lakeformation.types.transaction_description.TransactionDescription"
    ]
    """<p>Returns a <code>TransactionDescription</code> object containing information about the transaction.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeTransactionResponse) -> dict:
    out: dict = {}
    if "transaction_description" in value:
        import aws_sdk_lakeformation.types.transaction_description

        out["TransactionDescription"] = (
            aws_sdk_lakeformation.types.transaction_description.serialize_json(
                value["transaction_description"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeTransactionResponse:
    out: DescribeTransactionResponse = {}  # type: ignore[typeddict-item]
    if "TransactionDescription" in data:
        import aws_sdk_lakeformation.types.transaction_description

        out["transaction_description"] = (
            aws_sdk_lakeformation.types.transaction_description.deserialize_json(
                data["TransactionDescription"]
            )
        )
    return out
