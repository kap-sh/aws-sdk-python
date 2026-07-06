"""Generated from Smithy shape ``com.amazonaws.connect#RuleTriggerEventSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.event_source_name
    import aws_sdk_connect.types.integration_association_id


class RuleTriggerEventSource(TypedDict, closed=True):
    event_source_name: "aws_sdk_connect.types.event_source_name.EventSourceName"
    """<p>The name of the event source.</p>"""
    integration_association_id: NotRequired[
        "aws_sdk_connect.types.integration_association_id.IntegrationAssociationId"
    ]
    """<p>The identifier for the integration association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleTriggerEventSource) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.event_source_name

    out["EventSourceName"] = aws_sdk_connect.types.event_source_name.serialize_json(
        value["event_source_name"]
    )
    if "integration_association_id" in value:
        out["IntegrationAssociationId"] = value["integration_association_id"]
    return out


def deserialize_json(data: dict) -> RuleTriggerEventSource:
    out: RuleTriggerEventSource = {}  # type: ignore[typeddict-item]
    if "EventSourceName" in data:
        import aws_sdk_connect.types.event_source_name

        out["event_source_name"] = (
            aws_sdk_connect.types.event_source_name.deserialize_json(
                data["EventSourceName"]
            )
        )
    else:
        raise DeserializationError("RuleTriggerEventSource.event_source_name required")
    if "IntegrationAssociationId" in data:
        out["integration_association_id"] = data["IntegrationAssociationId"]
    return out
