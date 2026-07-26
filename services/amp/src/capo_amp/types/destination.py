"""Generated from Smithy shape ``com.amazonaws.amp#Destination``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_amp.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_amp.types.amp_configuration


class _Destination_ampConfiguration(TypedDict, closed=True):
    ampConfiguration: "capo_amp.types.amp_configuration.AmpConfiguration"


Destination: TypeAlias = _Destination_ampConfiguration


# --- restJson1 ser/de ---
def serialize_json(value: Destination) -> dict:
    if "ampConfiguration" in value:
        import capo_amp.types.amp_configuration

        return {
            "ampConfiguration": capo_amp.types.amp_configuration.serialize_json(
                value["ampConfiguration"]
            )
        }
    else:
        raise SerializationError("Destination: no variant present")


def deserialize_json(data: dict) -> Destination:
    if "ampConfiguration" in data:
        import capo_amp.types.amp_configuration

        return {
            "ampConfiguration": capo_amp.types.amp_configuration.deserialize_json(
                data["ampConfiguration"]
            )
        }
    else:
        raise DeserializationError("Destination: no recognized variant key")
