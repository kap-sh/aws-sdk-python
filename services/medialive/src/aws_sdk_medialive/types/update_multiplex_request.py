"""Generated from Smithy shape ``com.amazonaws.medialive#UpdateMultiplexRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.multiplex_packet_identifiers_mapping
    import aws_sdk_medialive.types.multiplex_settings


class UpdateMultiplexRequest(TypedDict):
    multiplex_id: "aws_sdk_medialive.types.__string.__string"
    """ID of the multiplex to update."""
    multiplex_settings: NotRequired[
        "aws_sdk_medialive.types.multiplex_settings.MultiplexSettings"
    ]
    """The new settings for a multiplex."""
    name: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Name of the multiplex."""
    packet_identifiers_mapping: NotRequired[
        "aws_sdk_medialive.types.multiplex_packet_identifiers_mapping.MultiplexPacketIdentifiersMapping"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMultiplexRequest) -> dict:
    out: dict = {}
    if "multiplex_settings" in value:
        import aws_sdk_medialive.types.multiplex_settings

        out["multiplexSettings"] = (
            aws_sdk_medialive.types.multiplex_settings.serialize_json(
                value["multiplex_settings"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "packet_identifiers_mapping" in value:
        import aws_sdk_medialive.types.multiplex_packet_identifiers_mapping

        out["packetIdentifiersMapping"] = (
            aws_sdk_medialive.types.multiplex_packet_identifiers_mapping.serialize_json(
                value["packet_identifiers_mapping"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateMultiplexRequest:
    out: UpdateMultiplexRequest = {}  # type: ignore[typeddict-item]
    if "multiplexSettings" in data:
        import aws_sdk_medialive.types.multiplex_settings

        out["multiplex_settings"] = (
            aws_sdk_medialive.types.multiplex_settings.deserialize_json(
                data["multiplexSettings"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    if "packetIdentifiersMapping" in data:
        import aws_sdk_medialive.types.multiplex_packet_identifiers_mapping

        out["packet_identifiers_mapping"] = (
            aws_sdk_medialive.types.multiplex_packet_identifiers_mapping.deserialize_json(
                data["packetIdentifiersMapping"]
            )
        )
    return out
