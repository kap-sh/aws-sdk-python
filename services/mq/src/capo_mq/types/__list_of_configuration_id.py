"""Generated from Smithy shape ``com.amazonaws.mq#__listOfConfigurationId``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mq.types.configuration_id

__listOfConfigurationId: TypeAlias = list[
    "capo_mq.types.configuration_id.ConfigurationId"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfConfigurationId) -> list:
    import capo_mq.types.configuration_id

    out: list = []
    for item in value:
        out.append(capo_mq.types.configuration_id.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfConfigurationId:
    import capo_mq.types.configuration_id

    out: __listOfConfigurationId = []
    for item in data:
        out.append(capo_mq.types.configuration_id.deserialize_json(item))
    return out
