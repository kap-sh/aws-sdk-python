"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.string
    import capo_ecs.types.timestamp


class ServiceEvent(TypedDict, closed=True):
    id: NotRequired["capo_ecs.types.string.String"]
    """<p>The ID string for the event.</p>"""
    created_at: NotRequired["capo_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the event was triggered.</p>"""
    message: NotRequired["capo_ecs.types.string.String"]
    """<p>The event message.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceEvent) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "created_at" in value:
        import capo_ecs.types.timestamp

        out["createdAt"] = capo_ecs.types.timestamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceEvent:
    out: ServiceEvent = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("createdAt") is not None:
        import capo_ecs.types.timestamp

        out["created_at"] = capo_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out
