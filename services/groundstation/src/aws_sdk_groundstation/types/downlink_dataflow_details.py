"""Generated from Smithy shape ``com.amazonaws.groundstation#DownlinkDataflowDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_groundstation.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.downlink_connection_details


class _DownlinkDataflowDetails_agentConnectionDetails(TypedDict, closed=True):
    agentConnectionDetails: "aws_sdk_groundstation.types.downlink_connection_details.DownlinkConnectionDetails"


DownlinkDataflowDetails: TypeAlias = _DownlinkDataflowDetails_agentConnectionDetails


# --- restJson1 ser/de ---
def serialize_json(value: DownlinkDataflowDetails) -> dict:
    if "agentConnectionDetails" in value:
        import aws_sdk_groundstation.types.downlink_connection_details

        return {
            "agentConnectionDetails": aws_sdk_groundstation.types.downlink_connection_details.serialize_json(
                value["agentConnectionDetails"]
            )
        }
    else:
        raise SerializationError("DownlinkDataflowDetails: no variant present")


def deserialize_json(data: dict) -> DownlinkDataflowDetails:
    if "agentConnectionDetails" in data:
        import aws_sdk_groundstation.types.downlink_connection_details

        return {
            "agentConnectionDetails": aws_sdk_groundstation.types.downlink_connection_details.deserialize_json(
                data["agentConnectionDetails"]
            )
        }
    else:
        raise DeserializationError("DownlinkDataflowDetails: no recognized variant key")
