"""Generated from Smithy shape ``com.amazonaws.mq#__listOfConfigurationRevision``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mq.types.configuration_revision

__listOfConfigurationRevision: TypeAlias = list[
    "aws_sdk_mq.types.configuration_revision.ConfigurationRevision"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfConfigurationRevision) -> list:
    import aws_sdk_mq.types.configuration_revision

    out: list = []
    for item in value:
        out.append(aws_sdk_mq.types.configuration_revision.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfConfigurationRevision:
    import aws_sdk_mq.types.configuration_revision

    out: __listOfConfigurationRevision = []
    for item in data:
        out.append(aws_sdk_mq.types.configuration_revision.deserialize_json(item))
    return out
