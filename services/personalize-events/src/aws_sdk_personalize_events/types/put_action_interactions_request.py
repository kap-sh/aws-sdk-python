"""Generated from Smithy shape ``com.amazonaws.personalizeevents#PutActionInteractionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_personalize_events.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_personalize_events.types.action_interactions_list
    import aws_sdk_personalize_events.types.string_type


class PutActionInteractionsRequest(TypedDict):
    tracking_id: "aws_sdk_personalize_events.types.string_type.StringType"
    """<p>The ID of your action interaction event tracker. When you create an Action interactions dataset, Amazon Personalize creates an action interaction event tracker for you. For more information, see <a href=\"https://docs.aws.amazon.com/personalize/latest/dg/action-interaction-tracker-id.html\">Action interaction event tracker ID</a>.</p>"""
    action_interactions: "aws_sdk_personalize_events.types.action_interactions_list.ActionInteractionsList"
    """<p>A list of action interaction events from the session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutActionInteractionsRequest) -> dict:
    out: dict = {}
    out["trackingId"] = value["tracking_id"]
    import aws_sdk_personalize_events.types.action_interactions_list

    out["actionInteractions"] = (
        aws_sdk_personalize_events.types.action_interactions_list.serialize_json(
            value["action_interactions"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutActionInteractionsRequest:
    out: PutActionInteractionsRequest = {}  # type: ignore[typeddict-item]
    if "trackingId" in data:
        out["tracking_id"] = data["trackingId"]
    else:
        raise DeserializationError("PutActionInteractionsRequest.tracking_id required")
    if "actionInteractions" in data:
        import aws_sdk_personalize_events.types.action_interactions_list

        out["action_interactions"] = (
            aws_sdk_personalize_events.types.action_interactions_list.deserialize_json(
                data["actionInteractions"]
            )
        )
    else:
        raise DeserializationError(
            "PutActionInteractionsRequest.action_interactions required"
        )
    return out
