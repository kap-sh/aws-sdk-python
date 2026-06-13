"""Generated from Smithy shape ``com.amazonaws.ssmincidents#SsmParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.ssm_parameter_values

SsmParameters: TypeAlias = dict[
    "str", "aws_sdk_ssm_incidents.types.ssm_parameter_values.SsmParameterValues"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: SsmParameters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_ssm_incidents.types.ssm_parameter_values

        out[key] = aws_sdk_ssm_incidents.types.ssm_parameter_values.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> SsmParameters:
    out: SsmParameters = {}
    for key, value in data.items():
        import aws_sdk_ssm_incidents.types.ssm_parameter_values

        out[key] = aws_sdk_ssm_incidents.types.ssm_parameter_values.deserialize_json(
            value
        )
    return out
