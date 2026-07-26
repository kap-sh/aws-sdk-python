"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CustomProtocolDetail``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.custom_protocol_detail_key
    import capo_iot_managed_integrations.types.custom_protocol_detail_value

CustomProtocolDetail: TypeAlias = dict[
    "capo_iot_managed_integrations.types.custom_protocol_detail_key.CustomProtocolDetailKey",
    "capo_iot_managed_integrations.types.custom_protocol_detail_value.CustomProtocolDetailValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: CustomProtocolDetail) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> CustomProtocolDetail:
    out: CustomProtocolDetail = {}
    for key, value in data.items():
        out[key] = value
    return out
