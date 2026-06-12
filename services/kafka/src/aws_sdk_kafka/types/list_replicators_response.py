"""Generated from Smithy shape ``com.amazonaws.kafka#ListReplicatorsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__list_of_replicator_summary
    import aws_sdk_kafka.types.__string


class ListReplicatorsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>If the response of ListReplicators is truncated, it returns a NextToken in the response. This NextToken should be sent in the subsequent request to ListReplicators.</p>"""
    replicators: NotRequired[
        "aws_sdk_kafka.types.__list_of_replicator_summary.__listOfReplicatorSummary"
    ]
    """<p>List containing information of each of the replicators in the account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListReplicatorsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "replicators" in value:
        import aws_sdk_kafka.types.__list_of_replicator_summary

        out["replicators"] = (
            aws_sdk_kafka.types.__list_of_replicator_summary.serialize_json(
                value["replicators"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListReplicatorsResponse:
    out: ListReplicatorsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "replicators" in data:
        import aws_sdk_kafka.types.__list_of_replicator_summary

        out["replicators"] = (
            aws_sdk_kafka.types.__list_of_replicator_summary.deserialize_json(
                data["replicators"]
            )
        )
    return out
