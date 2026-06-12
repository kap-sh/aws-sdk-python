"""Generated from Smithy shape ``com.amazonaws.codecommit#SetFileModeEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.set_file_mode_entry

SetFileModeEntries: TypeAlias = list[
    "aws_sdk_codecommit.types.set_file_mode_entry.SetFileModeEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetFileModeEntries) -> list:
    import aws_sdk_codecommit.types.set_file_mode_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codecommit.types.set_file_mode_entry.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SetFileModeEntries:
    import aws_sdk_codecommit.types.set_file_mode_entry

    out: SetFileModeEntries = []
    for item in data:
        out.append(
            aws_sdk_codecommit.types.set_file_mode_entry.deserialize_aws_json_1_1(item)
        )
    return out
