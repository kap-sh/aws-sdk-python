"""Generated from Smithy shape ``com.amazonaws.codecommit#PutFileEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.put_file_entry

PutFileEntries: TypeAlias = list["aws_sdk_codecommit.types.put_file_entry.PutFileEntry"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutFileEntries) -> list:
    import aws_sdk_codecommit.types.put_file_entry

    out: list = []
    for item in value:
        out.append(aws_sdk_codecommit.types.put_file_entry.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PutFileEntries:
    import aws_sdk_codecommit.types.put_file_entry

    out: PutFileEntries = []
    for item in data:
        out.append(
            aws_sdk_codecommit.types.put_file_entry.deserialize_aws_json_1_1(item)
        )
    return out
