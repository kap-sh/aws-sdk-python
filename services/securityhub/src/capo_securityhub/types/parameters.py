"""Generated from Smithy shape ``com.amazonaws.securityhub#Parameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.parameter_configuration

Parameters: TypeAlias = dict[
    "capo_securityhub.types.non_empty_string.NonEmptyString",
    "capo_securityhub.types.parameter_configuration.ParameterConfiguration",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: Parameters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_securityhub.types.parameter_configuration

        out[key] = capo_securityhub.types.parameter_configuration.serialize_json(value)
    return out


def deserialize_json(data: dict) -> Parameters:
    out: Parameters = {}
    for key, value in data.items():
        import capo_securityhub.types.parameter_configuration

        out[key] = capo_securityhub.types.parameter_configuration.deserialize_json(
            value
        )
    return out
