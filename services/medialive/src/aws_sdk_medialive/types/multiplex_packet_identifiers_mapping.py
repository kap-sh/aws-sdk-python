"""Generated from Smithy shape ``com.amazonaws.medialive#MultiplexPacketIdentifiersMapping``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.multiplex_program_packet_identifiers_map

MultiplexPacketIdentifiersMapping: TypeAlias = dict[
    "aws_sdk_medialive.types.__string.__string",
    "aws_sdk_medialive.types.multiplex_program_packet_identifiers_map.MultiplexProgramPacketIdentifiersMap",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: MultiplexPacketIdentifiersMapping) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_medialive.types.multiplex_program_packet_identifiers_map

        out[key] = (
            aws_sdk_medialive.types.multiplex_program_packet_identifiers_map.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> MultiplexPacketIdentifiersMapping:
    out: MultiplexPacketIdentifiersMapping = {}
    for key, value in data.items():
        import aws_sdk_medialive.types.multiplex_program_packet_identifiers_map

        out[key] = (
            aws_sdk_medialive.types.multiplex_program_packet_identifiers_map.deserialize_json(
                value
            )
        )
    return out
