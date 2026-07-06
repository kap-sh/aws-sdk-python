"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ServiceEventDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.service_event_metadata


class ServiceEventDetails(TypedDict, closed=True):
    title: "str"
    """<p>The title of the event.</p>"""
    description: "str"
    """<p>The description of the event.</p>"""
    event_metadata: NotRequired[
        "aws_sdk_resiliencehubv2.types.service_event_metadata.ServiceEventMetadata"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceEventDetails) -> dict:
    out: dict = {}
    out["title"] = value["title"]
    out["description"] = value["description"]
    if "event_metadata" in value:
        import aws_sdk_resiliencehubv2.types.service_event_metadata

        out["eventMetadata"] = (
            aws_sdk_resiliencehubv2.types.service_event_metadata.serialize_json(
                value["event_metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> ServiceEventDetails:
    out: ServiceEventDetails = {}  # type: ignore[typeddict-item]
    if "title" in data:
        out["title"] = data["title"]
    else:
        raise DeserializationError("ServiceEventDetails.title required")
    if "description" in data:
        out["description"] = data["description"]
    else:
        raise DeserializationError("ServiceEventDetails.description required")
    if "eventMetadata" in data:
        import aws_sdk_resiliencehubv2.types.service_event_metadata

        out["event_metadata"] = (
            aws_sdk_resiliencehubv2.types.service_event_metadata.deserialize_json(
                data["eventMetadata"]
            )
        )
    return out
