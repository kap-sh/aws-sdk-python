"""Generated from Smithy shape ``com.amazonaws.kendra#DocumentMetadataConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.document_metadata_configuration

DocumentMetadataConfigurationList: TypeAlias = list[
    "aws_sdk_kendra.types.document_metadata_configuration.DocumentMetadataConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentMetadataConfigurationList) -> list:
    import aws_sdk_kendra.types.document_metadata_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kendra.types.document_metadata_configuration.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DocumentMetadataConfigurationList:
    import aws_sdk_kendra.types.document_metadata_configuration

    out: DocumentMetadataConfigurationList = []
    for item in data:
        out.append(
            aws_sdk_kendra.types.document_metadata_configuration.deserialize_aws_json_1_1(
                item
            )
        )
    return out
