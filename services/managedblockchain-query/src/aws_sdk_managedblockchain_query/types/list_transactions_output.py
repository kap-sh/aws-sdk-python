"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#ListTransactionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_managedblockchain_query.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_managedblockchain_query.types.next_token
    import aws_sdk_managedblockchain_query.types.transaction_output_list


class ListTransactionsOutput(TypedDict, closed=True):
    transactions: "aws_sdk_managedblockchain_query.types.transaction_output_list.TransactionOutputList"
    """<p>The array of transactions returned by the request.</p>"""
    next_token: NotRequired[
        "aws_sdk_managedblockchain_query.types.next_token.NextToken"
    ]
    """<p>The pagination token that indicates the next set of results to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTransactionsOutput) -> dict:
    out: dict = {}
    import aws_sdk_managedblockchain_query.types.transaction_output_list

    out["transactions"] = (
        aws_sdk_managedblockchain_query.types.transaction_output_list.serialize_json(
            value["transactions"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTransactionsOutput:
    out: ListTransactionsOutput = {}  # type: ignore[typeddict-item]
    if "transactions" in data:
        import aws_sdk_managedblockchain_query.types.transaction_output_list

        out["transactions"] = (
            aws_sdk_managedblockchain_query.types.transaction_output_list.deserialize_json(
                data["transactions"]
            )
        )
    else:
        raise DeserializationError("ListTransactionsOutput.transactions required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
