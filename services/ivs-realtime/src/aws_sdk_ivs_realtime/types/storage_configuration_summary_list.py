"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#StorageConfigurationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.storage_configuration_summary

StorageConfigurationSummaryList: TypeAlias = list[
    "aws_sdk_ivs_realtime.types.storage_configuration_summary.StorageConfigurationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: StorageConfigurationSummaryList) -> list:
    import aws_sdk_ivs_realtime.types.storage_configuration_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ivs_realtime.types.storage_configuration_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> StorageConfigurationSummaryList:
    import aws_sdk_ivs_realtime.types.storage_configuration_summary

    out: StorageConfigurationSummaryList = []
    for item in data:
        out.append(
            aws_sdk_ivs_realtime.types.storage_configuration_summary.deserialize_json(
                item
            )
        )
    return out
