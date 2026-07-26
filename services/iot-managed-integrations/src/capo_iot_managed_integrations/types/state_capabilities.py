"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#StateCapabilities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.state_capability

StateCapabilities: TypeAlias = list[
    "capo_iot_managed_integrations.types.state_capability.StateCapability"
]


# --- restJson1 ser/de ---
def serialize_json(value: StateCapabilities) -> list:
    import capo_iot_managed_integrations.types.state_capability

    out: list = []
    for item in value:
        out.append(
            capo_iot_managed_integrations.types.state_capability.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> StateCapabilities:
    import capo_iot_managed_integrations.types.state_capability

    out: StateCapabilities = []
    for item in data:
        out.append(
            capo_iot_managed_integrations.types.state_capability.deserialize_json(item)
        )
    return out
