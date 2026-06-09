"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceEvent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.timestamp


class ServiceEvent(TypedDict):
    id: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ID string for the event.</p>"""
    created_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the event was triggered.</p>"""
    message: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The event message.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceEvent) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "created_at" in value:
        import aws_sdk_ecs.types.timestamp

        out["createdAt"] = aws_sdk_ecs.types.timestamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceEvent:
    out: ServiceEvent = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "createdAt" in data:
        import aws_sdk_ecs.types.timestamp

        out["created_at"] = aws_sdk_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    if "message" in data:
        out["message"] = data["message"]
    return out
