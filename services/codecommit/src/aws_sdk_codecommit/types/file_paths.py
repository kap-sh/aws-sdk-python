"""Generated from Smithy shape ``com.amazonaws.codecommit#FilePaths``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.path

FilePaths: TypeAlias = list["aws_sdk_codecommit.types.path.Path"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilePaths) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> FilePaths:
    return list(data)
