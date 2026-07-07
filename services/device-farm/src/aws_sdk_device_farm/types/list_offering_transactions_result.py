"""Generated from Smithy shape ``com.amazonaws.devicefarm#ListOfferingTransactionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.offering_transactions
    import aws_sdk_device_farm.types.pagination_token


class ListOfferingTransactionsResult(TypedDict, closed=True):
    offering_transactions: NotRequired[
        "aws_sdk_device_farm.types.offering_transactions.OfferingTransactions"
    ]
    """<p>The audit log of subscriptions you have purchased and modified through AWS Device Farm.</p>"""
    next_token: NotRequired[
        "aws_sdk_device_farm.types.pagination_token.PaginationToken"
    ]
    """<p>An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfferingTransactionsResult) -> dict:
    out: dict = {}
    if "offering_transactions" in value:
        import aws_sdk_device_farm.types.offering_transactions

        out["offeringTransactions"] = (
            aws_sdk_device_farm.types.offering_transactions.serialize_aws_json_1_1(
                value["offering_transactions"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListOfferingTransactionsResult:
    out: ListOfferingTransactionsResult = {}  # type: ignore[typeddict-item]
    if "offeringTransactions" in data:
        import aws_sdk_device_farm.types.offering_transactions

        out["offering_transactions"] = (
            aws_sdk_device_farm.types.offering_transactions.deserialize_aws_json_1_1(
                data["offeringTransactions"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
