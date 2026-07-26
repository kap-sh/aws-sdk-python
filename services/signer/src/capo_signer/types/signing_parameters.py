"""Generated from Smithy shape ``com.amazonaws.signer#SigningParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_signer.types.signing_parameter_key
    import capo_signer.types.signing_parameter_value

SigningParameters: TypeAlias = dict[
    "capo_signer.types.signing_parameter_key.SigningParameterKey",
    "capo_signer.types.signing_parameter_value.SigningParameterValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: SigningParameters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> SigningParameters:
    out: SigningParameters = {}
    for key, value in data.items():
        out[key] = value
    return out
