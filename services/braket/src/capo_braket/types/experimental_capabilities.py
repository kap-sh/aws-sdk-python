"""Generated from Smithy shape ``com.amazonaws.braket#ExperimentalCapabilities``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_braket.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_braket.types.experimental_capabilities_enablement_type


class _ExperimentalCapabilities_enabled(TypedDict, closed=True):
    enabled: "capo_braket.types.experimental_capabilities_enablement_type.ExperimentalCapabilitiesEnablementType"


ExperimentalCapabilities: TypeAlias = _ExperimentalCapabilities_enabled


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentalCapabilities) -> dict:
    if "enabled" in value:
        return {"enabled": value["enabled"]}
    else:
        raise SerializationError("ExperimentalCapabilities: no variant present")


def deserialize_json(data: dict) -> ExperimentalCapabilities:
    if "enabled" in data:
        return {"enabled": data["enabled"]}
    else:
        raise DeserializationError(
            "ExperimentalCapabilities: no recognized variant key"
        )
