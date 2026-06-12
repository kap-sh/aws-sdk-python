"""Generated from Smithy shape ``com.amazonaws.directoryservice#SharedDirectories``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.shared_directory

SharedDirectories: TypeAlias = list[
    "aws_sdk_directory_service.types.shared_directory.SharedDirectory"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SharedDirectories) -> list:
    import aws_sdk_directory_service.types.shared_directory

    out: list = []
    for item in value:
        out.append(
            aws_sdk_directory_service.types.shared_directory.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SharedDirectories:
    import aws_sdk_directory_service.types.shared_directory

    out: SharedDirectories = []
    for item in data:
        out.append(
            aws_sdk_directory_service.types.shared_directory.deserialize_aws_json_1_1(
                item
            )
        )
    return out
