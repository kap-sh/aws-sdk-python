"""Generated from Smithy shape ``com.amazonaws.connect#EmailAddressConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.email_address_config

EmailAddressConfigList: TypeAlias = list[
    "capo_connect.types.email_address_config.EmailAddressConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: EmailAddressConfigList) -> list:
    import capo_connect.types.email_address_config

    out: list = []
    for item in value:
        out.append(capo_connect.types.email_address_config.serialize_json(item))
    return out


def deserialize_json(data: list) -> EmailAddressConfigList:
    import capo_connect.types.email_address_config

    out: EmailAddressConfigList = []
    for item in data:
        out.append(capo_connect.types.email_address_config.deserialize_json(item))
    return out
