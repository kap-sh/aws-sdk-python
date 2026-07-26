"""Generated from Smithy shape ``com.amazonaws.mq#__listOfConfigurationRevision``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mq.types.configuration_revision

__listOfConfigurationRevision: TypeAlias = list[
    "capo_mq.types.configuration_revision.ConfigurationRevision"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfConfigurationRevision) -> list:
    import capo_mq.types.configuration_revision

    out: list = []
    for item in value:
        out.append(capo_mq.types.configuration_revision.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfConfigurationRevision:
    import capo_mq.types.configuration_revision

    out: __listOfConfigurationRevision = []
    for item in data:
        out.append(capo_mq.types.configuration_revision.deserialize_json(item))
    return out
