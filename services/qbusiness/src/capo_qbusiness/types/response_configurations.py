"""Generated from Smithy shape ``com.amazonaws.qbusiness#ResponseConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qbusiness.types.response_configuration
    import capo_qbusiness.types.response_configuration_type

ResponseConfigurations: TypeAlias = dict[
    "capo_qbusiness.types.response_configuration_type.ResponseConfigurationType",
    "capo_qbusiness.types.response_configuration.ResponseConfiguration",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ResponseConfigurations) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_qbusiness.types.response_configuration
        import capo_qbusiness.types.response_configuration_type

        out[capo_qbusiness.types.response_configuration_type.serialize_json(key)] = (
            capo_qbusiness.types.response_configuration.serialize_json(value)
        )
    return out


def deserialize_json(data: dict) -> ResponseConfigurations:
    out: ResponseConfigurations = {}
    for key, value in data.items():
        import capo_qbusiness.types.response_configuration
        import capo_qbusiness.types.response_configuration_type

        out[capo_qbusiness.types.response_configuration_type.deserialize_json(key)] = (
            capo_qbusiness.types.response_configuration.deserialize_json(value)
        )
    return out
