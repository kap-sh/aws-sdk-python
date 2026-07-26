"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#StorageConfigurationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ivs_realtime.types.storage_configuration_summary

StorageConfigurationSummaryList: TypeAlias = list[
    "capo_ivs_realtime.types.storage_configuration_summary.StorageConfigurationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: StorageConfigurationSummaryList) -> list:
    import capo_ivs_realtime.types.storage_configuration_summary

    out: list = []
    for item in value:
        out.append(
            capo_ivs_realtime.types.storage_configuration_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> StorageConfigurationSummaryList:
    import capo_ivs_realtime.types.storage_configuration_summary

    out: StorageConfigurationSummaryList = []
    for item in data:
        out.append(
            capo_ivs_realtime.types.storage_configuration_summary.deserialize_json(item)
        )
    return out
