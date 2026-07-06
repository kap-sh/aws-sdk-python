"""Generated from Smithy shape ``com.amazonaws.mq#ListBrokersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mq.types.__list_of_broker_summary
    import aws_sdk_mq.types.__string


class ListBrokersResponse(TypedDict, closed=True):
    broker_summaries: NotRequired[
        "aws_sdk_mq.types.__list_of_broker_summary.__listOfBrokerSummary"
    ]
    """<p>A list of information about all brokers.</p>"""
    next_token: NotRequired["aws_sdk_mq.types.__string.__string"]
    """<p>The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBrokersResponse) -> dict:
    out: dict = {}
    if "broker_summaries" in value:
        import aws_sdk_mq.types.__list_of_broker_summary

        out["brokerSummaries"] = (
            aws_sdk_mq.types.__list_of_broker_summary.serialize_json(
                value["broker_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBrokersResponse:
    out: ListBrokersResponse = {}  # type: ignore[typeddict-item]
    if "brokerSummaries" in data:
        import aws_sdk_mq.types.__list_of_broker_summary

        out["broker_summaries"] = (
            aws_sdk_mq.types.__list_of_broker_summary.deserialize_json(
                data["brokerSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
