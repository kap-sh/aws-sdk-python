"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#ListFilteredTransactionEventsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_managedblockchain_query.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_managedblockchain_query.types.next_token
    import aws_sdk_managedblockchain_query.types.transaction_event_list


class ListFilteredTransactionEventsOutput(TypedDict):
    events: "aws_sdk_managedblockchain_query.types.transaction_event_list.TransactionEventList"
    """<p>The transaction events returned by the request.</p>"""
    next_token: NotRequired[
        "aws_sdk_managedblockchain_query.types.next_token.NextToken"
    ]
    """<p>The pagination token that indicates the next set of results to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFilteredTransactionEventsOutput) -> dict:
    out: dict = {}
    import aws_sdk_managedblockchain_query.types.transaction_event_list

    out["events"] = (
        aws_sdk_managedblockchain_query.types.transaction_event_list.serialize_json(
            value["events"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFilteredTransactionEventsOutput:
    out: ListFilteredTransactionEventsOutput = {}  # type: ignore[typeddict-item]
    if "events" in data:
        import aws_sdk_managedblockchain_query.types.transaction_event_list

        out["events"] = (
            aws_sdk_managedblockchain_query.types.transaction_event_list.deserialize_json(
                data["events"]
            )
        )
    else:
        raise DeserializationError(
            "ListFilteredTransactionEventsOutput.events required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
