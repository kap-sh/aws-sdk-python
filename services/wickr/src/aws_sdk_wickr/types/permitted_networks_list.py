"""Generated from Smithy shape ``com.amazonaws.wickr#PermittedNetworksList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wickr.types.network_id

PermittedNetworksList: TypeAlias = list["aws_sdk_wickr.types.network_id.NetworkId"]


# --- restJson1 ser/de ---
def serialize_json(value: PermittedNetworksList) -> list:
    return list(value)


def deserialize_json(data: list) -> PermittedNetworksList:
    return list(data)
