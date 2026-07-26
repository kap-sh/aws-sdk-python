"""Generated from Smithy shape ``com.amazonaws.drs#EventResourceData``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_drs.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_drs.types.source_network_data


class _EventResourceData_sourceNetworkData(TypedDict, closed=True):
    sourceNetworkData: "capo_drs.types.source_network_data.SourceNetworkData"


EventResourceData: TypeAlias = _EventResourceData_sourceNetworkData


# --- restJson1 ser/de ---
def serialize_json(value: EventResourceData) -> dict:
    if "sourceNetworkData" in value:
        import capo_drs.types.source_network_data

        return {
            "sourceNetworkData": capo_drs.types.source_network_data.serialize_json(
                value["sourceNetworkData"]
            )
        }
    else:
        raise SerializationError("EventResourceData: no variant present")


def deserialize_json(data: dict) -> EventResourceData:
    if "sourceNetworkData" in data:
        import capo_drs.types.source_network_data

        return {
            "sourceNetworkData": capo_drs.types.source_network_data.deserialize_json(
                data["sourceNetworkData"]
            )
        }
    else:
        raise DeserializationError("EventResourceData: no recognized variant key")
