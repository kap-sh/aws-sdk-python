"""Generated from Smithy shape ``com.amazonaws.connect#AfterContactWorkConfigs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.after_contact_work_config_per_channel

AfterContactWorkConfigs: TypeAlias = list[
    "capo_connect.types.after_contact_work_config_per_channel.AfterContactWorkConfigPerChannel"
]


# --- restJson1 ser/de ---
def serialize_json(value: AfterContactWorkConfigs) -> list:
    import capo_connect.types.after_contact_work_config_per_channel

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.after_contact_work_config_per_channel.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AfterContactWorkConfigs:
    import capo_connect.types.after_contact_work_config_per_channel

    out: AfterContactWorkConfigs = []
    for item in data:
        out.append(
            capo_connect.types.after_contact_work_config_per_channel.deserialize_json(
                item
            )
        )
    return out
