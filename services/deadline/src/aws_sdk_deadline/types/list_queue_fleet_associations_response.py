"""Generated from Smithy shape ``com.amazonaws.deadline#ListQueueFleetAssociationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.next_token
    import aws_sdk_deadline.types.queue_fleet_association_summaries


class ListQueueFleetAssociationsResponse(TypedDict, closed=True):
    queue_fleet_associations: "aws_sdk_deadline.types.queue_fleet_association_summaries.QueueFleetAssociationSummaries"
    """<p>The queue-fleet associations on the list.</p>"""
    next_token: NotRequired["aws_sdk_deadline.types.next_token.NextToken"]
    """<p>If Deadline Cloud returns <code>nextToken</code>, then there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. To retrieve the next page, call the operation again using the returned token. Keep all other arguments unchanged. If no results remain, then <code>nextToken</code> is set to <code>null</code>. Each pagination token expires after 24 hours. If you provide a token that isn't valid, then you receive an HTTP 400 <code>ValidationException</code> error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListQueueFleetAssociationsResponse) -> dict:
    out: dict = {}
    import aws_sdk_deadline.types.queue_fleet_association_summaries

    out["queueFleetAssociations"] = (
        aws_sdk_deadline.types.queue_fleet_association_summaries.serialize_json(
            value["queue_fleet_associations"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListQueueFleetAssociationsResponse:
    out: ListQueueFleetAssociationsResponse = {}  # type: ignore[typeddict-item]
    if "queueFleetAssociations" in data:
        import aws_sdk_deadline.types.queue_fleet_association_summaries

        out["queue_fleet_associations"] = (
            aws_sdk_deadline.types.queue_fleet_association_summaries.deserialize_json(
                data["queueFleetAssociations"]
            )
        )
    else:
        raise DeserializationError(
            "ListQueueFleetAssociationsResponse.queue_fleet_associations required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
