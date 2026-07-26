"""Generated from Smithy shape ``com.amazonaws.qbusiness#AuthorizationResponseMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qbusiness.types.auth_response_key
    import capo_qbusiness.types.auth_response_value

AuthorizationResponseMap: TypeAlias = dict[
    "capo_qbusiness.types.auth_response_key.AuthResponseKey",
    "capo_qbusiness.types.auth_response_value.AuthResponseValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AuthorizationResponseMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> AuthorizationResponseMap:
    out: AuthorizationResponseMap = {}
    for key, value in data.items():
        out[key] = value
    return out
