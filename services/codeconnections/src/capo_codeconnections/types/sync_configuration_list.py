"""Generated from Smithy shape ``com.amazonaws.codeconnections#SyncConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeconnections.types.sync_configuration

SyncConfigurationList: TypeAlias = list[
    "capo_codeconnections.types.sync_configuration.SyncConfiguration"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SyncConfigurationList) -> list:
    import capo_codeconnections.types.sync_configuration

    out: list = []
    for item in value:
        out.append(
            capo_codeconnections.types.sync_configuration.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> SyncConfigurationList:
    import capo_codeconnections.types.sync_configuration

    out: SyncConfigurationList = []
    for item in data:
        out.append(
            capo_codeconnections.types.sync_configuration.deserialize_aws_json_1_0(item)
        )
    return out
