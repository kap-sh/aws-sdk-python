"""Generated from Smithy shape ``com.amazonaws.ssmincidents#DynamicSsmParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm_incidents.types.dynamic_ssm_parameter_value

DynamicSsmParameters: TypeAlias = dict[
    "str",
    "capo_ssm_incidents.types.dynamic_ssm_parameter_value.DynamicSsmParameterValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: DynamicSsmParameters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_ssm_incidents.types.dynamic_ssm_parameter_value

        out[key] = capo_ssm_incidents.types.dynamic_ssm_parameter_value.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> DynamicSsmParameters:
    out: DynamicSsmParameters = {}
    for key, value in data.items():
        import capo_ssm_incidents.types.dynamic_ssm_parameter_value

        out[key] = (
            capo_ssm_incidents.types.dynamic_ssm_parameter_value.deserialize_json(value)
        )
    return out
