"""Generated from Smithy shape ``com.amazonaws.codecommit#DeleteFileEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codecommit.types.delete_file_entry

DeleteFileEntries: TypeAlias = list[
    "capo_codecommit.types.delete_file_entry.DeleteFileEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteFileEntries) -> list:
    import capo_codecommit.types.delete_file_entry

    out: list = []
    for item in value:
        out.append(capo_codecommit.types.delete_file_entry.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DeleteFileEntries:
    import capo_codecommit.types.delete_file_entry

    out: DeleteFileEntries = []
    for item in data:
        out.append(
            capo_codecommit.types.delete_file_entry.deserialize_aws_json_1_1(item)
        )
    return out
