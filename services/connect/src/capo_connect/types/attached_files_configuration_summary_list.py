"""Generated from Smithy shape ``com.amazonaws.connect#AttachedFilesConfigurationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.attached_files_configuration_summary

AttachedFilesConfigurationSummaryList: TypeAlias = list[
    "capo_connect.types.attached_files_configuration_summary.AttachedFilesConfigurationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AttachedFilesConfigurationSummaryList) -> list:
    import capo_connect.types.attached_files_configuration_summary

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.attached_files_configuration_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AttachedFilesConfigurationSummaryList:
    import capo_connect.types.attached_files_configuration_summary

    out: AttachedFilesConfigurationSummaryList = []
    for item in data:
        out.append(
            capo_connect.types.attached_files_configuration_summary.deserialize_json(
                item
            )
        )
    return out
