"""Generated from Smithy shape ``com.amazonaws.connectcases#EventBridgeConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.event_included_data


class EventBridgeConfiguration(TypedDict):
    enabled: "bool"
    """<p>Indicates whether the to broadcast case event data to the customer.</p>"""
    included_data: NotRequired[
        "aws_sdk_connectcases.types.event_included_data.EventIncludedData"
    ]
    """<p>Details of what case and related item data is published through the case event stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventBridgeConfiguration) -> dict:
    out: dict = {}
    out["enabled"] = value["enabled"]
    if "included_data" in value:
        import aws_sdk_connectcases.types.event_included_data

        out["includedData"] = (
            aws_sdk_connectcases.types.event_included_data.serialize_json(
                value["included_data"]
            )
        )
    return out


def deserialize_json(data: dict) -> EventBridgeConfiguration:
    out: EventBridgeConfiguration = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    else:
        raise DeserializationError("EventBridgeConfiguration.enabled required")
    if "includedData" in data:
        import aws_sdk_connectcases.types.event_included_data

        out["included_data"] = (
            aws_sdk_connectcases.types.event_included_data.deserialize_json(
                data["includedData"]
            )
        )
    return out
