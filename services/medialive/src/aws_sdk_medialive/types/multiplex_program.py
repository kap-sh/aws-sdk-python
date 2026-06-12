"""Generated from Smithy shape ``com.amazonaws.medialive#MultiplexProgram``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_multiplex_program_pipeline_detail
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.multiplex_program_packet_identifiers_map
    import aws_sdk_medialive.types.multiplex_program_settings


class MultiplexProgram(TypedDict):
    channel_id: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The MediaLive channel associated with the program."""
    multiplex_program_settings: NotRequired[
        "aws_sdk_medialive.types.multiplex_program_settings.MultiplexProgramSettings"
    ]
    """The settings for this multiplex program."""
    packet_identifiers_map: NotRequired[
        "aws_sdk_medialive.types.multiplex_program_packet_identifiers_map.MultiplexProgramPacketIdentifiersMap"
    ]
    """The packet identifier map for this multiplex program."""
    pipeline_details: NotRequired[
        "aws_sdk_medialive.types.__list_of_multiplex_program_pipeline_detail.__listOfMultiplexProgramPipelineDetail"
    ]
    """Contains information about the current sources for the specified program in the specified multiplex. Keep in mind that each multiplex pipeline connects to both pipelines in a given source channel (the channel identified by the program). But only one of those channel pipelines is ever active at one time."""
    program_name: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The name of the multiplex program."""


# --- restJson1 ser/de ---
def serialize_json(value: MultiplexProgram) -> dict:
    out: dict = {}
    if "channel_id" in value:
        out["channelId"] = value["channel_id"]
    if "multiplex_program_settings" in value:
        import aws_sdk_medialive.types.multiplex_program_settings

        out["multiplexProgramSettings"] = (
            aws_sdk_medialive.types.multiplex_program_settings.serialize_json(
                value["multiplex_program_settings"]
            )
        )
    if "packet_identifiers_map" in value:
        import aws_sdk_medialive.types.multiplex_program_packet_identifiers_map

        out["packetIdentifiersMap"] = (
            aws_sdk_medialive.types.multiplex_program_packet_identifiers_map.serialize_json(
                value["packet_identifiers_map"]
            )
        )
    if "pipeline_details" in value:
        import aws_sdk_medialive.types.__list_of_multiplex_program_pipeline_detail

        out["pipelineDetails"] = (
            aws_sdk_medialive.types.__list_of_multiplex_program_pipeline_detail.serialize_json(
                value["pipeline_details"]
            )
        )
    if "program_name" in value:
        out["programName"] = value["program_name"]
    return out


def deserialize_json(data: dict) -> MultiplexProgram:
    out: MultiplexProgram = {}  # type: ignore[typeddict-item]
    if "channelId" in data:
        out["channel_id"] = data["channelId"]
    if "multiplexProgramSettings" in data:
        import aws_sdk_medialive.types.multiplex_program_settings

        out["multiplex_program_settings"] = (
            aws_sdk_medialive.types.multiplex_program_settings.deserialize_json(
                data["multiplexProgramSettings"]
            )
        )
    if "packetIdentifiersMap" in data:
        import aws_sdk_medialive.types.multiplex_program_packet_identifiers_map

        out["packet_identifiers_map"] = (
            aws_sdk_medialive.types.multiplex_program_packet_identifiers_map.deserialize_json(
                data["packetIdentifiersMap"]
            )
        )
    if "pipelineDetails" in data:
        import aws_sdk_medialive.types.__list_of_multiplex_program_pipeline_detail

        out["pipeline_details"] = (
            aws_sdk_medialive.types.__list_of_multiplex_program_pipeline_detail.deserialize_json(
                data["pipelineDetails"]
            )
        )
    if "programName" in data:
        out["program_name"] = data["programName"]
    return out
