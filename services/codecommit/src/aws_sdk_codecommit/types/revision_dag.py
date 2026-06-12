"""Generated from Smithy shape ``com.amazonaws.codecommit#RevisionDag``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.file_version

RevisionDag: TypeAlias = list["aws_sdk_codecommit.types.file_version.FileVersion"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RevisionDag) -> list:
    import aws_sdk_codecommit.types.file_version

    out: list = []
    for item in value:
        out.append(aws_sdk_codecommit.types.file_version.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RevisionDag:
    import aws_sdk_codecommit.types.file_version

    out: RevisionDag = []
    for item in data:
        out.append(aws_sdk_codecommit.types.file_version.deserialize_aws_json_1_1(item))
    return out
