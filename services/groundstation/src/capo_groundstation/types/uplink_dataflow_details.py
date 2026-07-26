"""Generated from Smithy shape ``com.amazonaws.groundstation#UplinkDataflowDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_groundstation.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_groundstation.types.uplink_connection_details


class _UplinkDataflowDetails_agentConnectionDetails(TypedDict, closed=True):
    agentConnectionDetails: (
        "capo_groundstation.types.uplink_connection_details.UplinkConnectionDetails"
    )


UplinkDataflowDetails: TypeAlias = _UplinkDataflowDetails_agentConnectionDetails


# --- restJson1 ser/de ---
def serialize_json(value: UplinkDataflowDetails) -> dict:
    if "agentConnectionDetails" in value:
        import capo_groundstation.types.uplink_connection_details

        return {
            "agentConnectionDetails": capo_groundstation.types.uplink_connection_details.serialize_json(
                value["agentConnectionDetails"]
            )
        }
    else:
        raise SerializationError("UplinkDataflowDetails: no variant present")


def deserialize_json(data: dict) -> UplinkDataflowDetails:
    if "agentConnectionDetails" in data:
        import capo_groundstation.types.uplink_connection_details

        return {
            "agentConnectionDetails": capo_groundstation.types.uplink_connection_details.deserialize_json(
                data["agentConnectionDetails"]
            )
        }
    else:
        raise DeserializationError("UplinkDataflowDetails: no recognized variant key")
