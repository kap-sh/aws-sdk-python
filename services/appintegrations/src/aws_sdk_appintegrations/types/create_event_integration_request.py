"""Generated from Smithy shape ``com.amazonaws.appintegrations#CreateEventIntegrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_appintegrations.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appintegrations.types.description
    import aws_sdk_appintegrations.types.event_bridge_bus
    import aws_sdk_appintegrations.types.event_filter
    import aws_sdk_appintegrations.types.idempotency_token
    import aws_sdk_appintegrations.types.name
    import aws_sdk_appintegrations.types.tag_map


class CreateEventIntegrationRequest(TypedDict, closed=True):
    name: "aws_sdk_appintegrations.types.name.Name"
    """<p>The name of the event integration.</p>"""
    description: NotRequired["aws_sdk_appintegrations.types.description.Description"]
    """<p>The description of the event integration.</p>"""
    event_filter: "aws_sdk_appintegrations.types.event_filter.EventFilter"
    """<p>The event filter.</p>"""
    event_bridge_bus: "aws_sdk_appintegrations.types.event_bridge_bus.EventBridgeBus"
    """<p>The EventBridge bus.</p>"""
    client_token: NotRequired[
        "aws_sdk_appintegrations.types.idempotency_token.IdempotencyToken"
    ]
    r"""<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href=\"https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\">Making retries safe with idempotent APIs</a>.</p>"""
    tags: NotRequired["aws_sdk_appintegrations.types.tag_map.TagMap"]
    r"""<p>The tags used to organize, track, or control access for this resource. For example, { \"tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEventIntegrationRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import aws_sdk_appintegrations.types.event_filter

    out["EventFilter"] = aws_sdk_appintegrations.types.event_filter.serialize_json(
        value["event_filter"]
    )
    out["EventBridgeBus"] = value["event_bridge_bus"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "tags" in value:
        import aws_sdk_appintegrations.types.tag_map

        out["Tags"] = aws_sdk_appintegrations.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateEventIntegrationRequest:
    out: CreateEventIntegrationRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateEventIntegrationRequest.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "EventFilter" in data:
        import aws_sdk_appintegrations.types.event_filter

        out["event_filter"] = (
            aws_sdk_appintegrations.types.event_filter.deserialize_json(
                data["EventFilter"]
            )
        )
    else:
        raise DeserializationError(
            "CreateEventIntegrationRequest.event_filter required"
        )
    if "EventBridgeBus" in data:
        out["event_bridge_bus"] = data["EventBridgeBus"]
    else:
        raise DeserializationError(
            "CreateEventIntegrationRequest.event_bridge_bus required"
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "Tags" in data:
        import aws_sdk_appintegrations.types.tag_map

        out["tags"] = aws_sdk_appintegrations.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out
