"""Generated from Smithy shape ``com.amazonaws.connectcases#SlaInputContent``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_connectcases.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.sla_input_configuration


class _SlaInputContent_slaInputConfiguration(TypedDict):
    slaInputConfiguration: (
        "aws_sdk_connectcases.types.sla_input_configuration.SlaInputConfiguration"
    )


SlaInputContent: TypeAlias = _SlaInputContent_slaInputConfiguration


# --- restJson1 ser/de ---
def serialize_json(value: SlaInputContent) -> dict:
    if "slaInputConfiguration" in value:
        import aws_sdk_connectcases.types.sla_input_configuration

        return {
            "slaInputConfiguration": aws_sdk_connectcases.types.sla_input_configuration.serialize_json(
                value["slaInputConfiguration"]
            )
        }
    else:
        raise SerializationError("SlaInputContent: no variant present")


def deserialize_json(data: dict) -> SlaInputContent:
    if "slaInputConfiguration" in data:
        import aws_sdk_connectcases.types.sla_input_configuration

        return {
            "slaInputConfiguration": aws_sdk_connectcases.types.sla_input_configuration.deserialize_json(
                data["slaInputConfiguration"]
            )
        }
    else:
        raise DeserializationError("SlaInputContent: no recognized variant key")
