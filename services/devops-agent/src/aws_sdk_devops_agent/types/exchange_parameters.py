"""Generated from Smithy shape ``com.amazonaws.devopsagent#ExchangeParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.exchange_parameter_value

ExchangeParameters: TypeAlias = dict[
    "str", "aws_sdk_devops_agent.types.exchange_parameter_value.ExchangeParameterValue"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ExchangeParameters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ExchangeParameters:
    out: ExchangeParameters = {}
    for key, value in data.items():
        out[key] = value
    return out
