"""Generated from Smithy shape ``com.amazonaws.drs#ParticipatingResourceID``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_drs.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_drs.types.source_network_id


class _ParticipatingResourceID_sourceNetworkID(TypedDict):
    sourceNetworkID: "aws_sdk_drs.types.source_network_id.SourceNetworkID"


ParticipatingResourceID: TypeAlias = _ParticipatingResourceID_sourceNetworkID


# --- restJson1 ser/de ---
def serialize_json(value: ParticipatingResourceID) -> dict:
    if "sourceNetworkID" in value:
        return {"sourceNetworkID": value["sourceNetworkID"]}
    else:
        raise SerializationError("ParticipatingResourceID: no variant present")


def deserialize_json(data: dict) -> ParticipatingResourceID:
    if "sourceNetworkID" in data:
        return {"sourceNetworkID": data["sourceNetworkID"]}
    else:
        raise DeserializationError("ParticipatingResourceID: no recognized variant key")
