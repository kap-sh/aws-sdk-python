"""Generated from Smithy shape ``com.amazonaws.lakeformation#ListTransactionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.token_string
    import aws_sdk_lakeformation.types.transaction_description_list


class ListTransactionsResponse(TypedDict):
    transactions: NotRequired[
        "aws_sdk_lakeformation.types.transaction_description_list.TransactionDescriptionList"
    ]
    """<p>A list of transactions. The record for each transaction is a <code>TransactionDescription</code> object.</p>"""
    next_token: NotRequired["aws_sdk_lakeformation.types.token_string.TokenString"]
    """<p>A continuation token indicating whether additional data is available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTransactionsResponse) -> dict:
    out: dict = {}
    if "transactions" in value:
        import aws_sdk_lakeformation.types.transaction_description_list

        out["Transactions"] = (
            aws_sdk_lakeformation.types.transaction_description_list.serialize_json(
                value["transactions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTransactionsResponse:
    out: ListTransactionsResponse = {}  # type: ignore[typeddict-item]
    if "Transactions" in data:
        import aws_sdk_lakeformation.types.transaction_description_list

        out["transactions"] = (
            aws_sdk_lakeformation.types.transaction_description_list.deserialize_json(
                data["Transactions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
