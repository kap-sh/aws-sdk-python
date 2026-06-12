"""Generated from Smithy shape ``com.amazonaws.directoryservice#SchemaExtensionsInfo``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.schema_extension_info

SchemaExtensionsInfo: TypeAlias = list[
    "aws_sdk_directory_service.types.schema_extension_info.SchemaExtensionInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SchemaExtensionsInfo) -> list:
    import aws_sdk_directory_service.types.schema_extension_info

    out: list = []
    for item in value:
        out.append(
            aws_sdk_directory_service.types.schema_extension_info.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SchemaExtensionsInfo:
    import aws_sdk_directory_service.types.schema_extension_info

    out: SchemaExtensionsInfo = []
    for item in data:
        out.append(
            aws_sdk_directory_service.types.schema_extension_info.deserialize_aws_json_1_1(
                item
            )
        )
    return out
