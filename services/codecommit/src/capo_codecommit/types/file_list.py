"""Generated from Smithy shape ``com.amazonaws.codecommit#FileList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codecommit.types.file

FileList: TypeAlias = list["capo_codecommit.types.file.File"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileList) -> list:
    import capo_codecommit.types.file

    out: list = []
    for item in value:
        out.append(capo_codecommit.types.file.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FileList:
    import capo_codecommit.types.file

    out: FileList = []
    for item in data:
        out.append(capo_codecommit.types.file.deserialize_aws_json_1_1(item))
    return out
