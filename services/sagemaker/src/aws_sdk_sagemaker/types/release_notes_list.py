"""Generated from Smithy shape ``com.amazonaws.sagemaker#ReleaseNotesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.string1024

ReleaseNotesList: TypeAlias = list["aws_sdk_sagemaker.types.string1024.String1024"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReleaseNotesList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ReleaseNotesList:
    return list(data)
