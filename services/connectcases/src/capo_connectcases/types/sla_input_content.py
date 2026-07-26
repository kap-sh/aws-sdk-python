"""Generated from Smithy shape ``com.amazonaws.connectcases#SlaInputContent``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connectcases.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_connectcases.types.sla_input_configuration


class _SlaInputContent_slaInputConfiguration(TypedDict, closed=True):
    slaInputConfiguration: (
        "capo_connectcases.types.sla_input_configuration.SlaInputConfiguration"
    )


SlaInputContent: TypeAlias = _SlaInputContent_slaInputConfiguration


# --- restJson1 ser/de ---
def serialize_json(value: SlaInputContent) -> dict:
    if "slaInputConfiguration" in value:
        import capo_connectcases.types.sla_input_configuration

        return {
            "slaInputConfiguration": capo_connectcases.types.sla_input_configuration.serialize_json(
                value["slaInputConfiguration"]
            )
        }
    else:
        raise SerializationError("SlaInputContent: no variant present")


def deserialize_json(data: dict) -> SlaInputContent:
    if "slaInputConfiguration" in data:
        import capo_connectcases.types.sla_input_configuration

        return {
            "slaInputConfiguration": capo_connectcases.types.sla_input_configuration.deserialize_json(
                data["slaInputConfiguration"]
            )
        }
    else:
        raise DeserializationError("SlaInputContent: no recognized variant key")
