"""Generated from Smithy shape ``com.amazonaws.connect#PhoneNumberConfigs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.phone_number_config

PhoneNumberConfigs: TypeAlias = list[
    "capo_connect.types.phone_number_config.PhoneNumberConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: PhoneNumberConfigs) -> list:
    import capo_connect.types.phone_number_config

    out: list = []
    for item in value:
        out.append(capo_connect.types.phone_number_config.serialize_json(item))
    return out


def deserialize_json(data: list) -> PhoneNumberConfigs:
    import capo_connect.types.phone_number_config

    out: PhoneNumberConfigs = []
    for item in data:
        out.append(capo_connect.types.phone_number_config.deserialize_json(item))
    return out
