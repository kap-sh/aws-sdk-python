"""Generated from Smithy shape ``com.amazonaws.connect#AttachedFilesConfigurationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.attached_files_configuration_summary

AttachedFilesConfigurationSummaryList: TypeAlias = list[
    "aws_sdk_connect.types.attached_files_configuration_summary.AttachedFilesConfigurationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AttachedFilesConfigurationSummaryList) -> list:
    import aws_sdk_connect.types.attached_files_configuration_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.attached_files_configuration_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AttachedFilesConfigurationSummaryList:
    import aws_sdk_connect.types.attached_files_configuration_summary

    out: AttachedFilesConfigurationSummaryList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.attached_files_configuration_summary.deserialize_json(
                item
            )
        )
    return out
