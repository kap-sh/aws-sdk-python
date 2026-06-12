"""Generated from Smithy shape ``com.amazonaws.fsx#CreateFileCacheDataRepositoryAssociations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fsx.types.file_cache_data_repository_association

CreateFileCacheDataRepositoryAssociations: TypeAlias = list[
    "aws_sdk_fsx.types.file_cache_data_repository_association.FileCacheDataRepositoryAssociation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateFileCacheDataRepositoryAssociations) -> list:
    import aws_sdk_fsx.types.file_cache_data_repository_association

    out: list = []
    for item in value:
        out.append(
            aws_sdk_fsx.types.file_cache_data_repository_association.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CreateFileCacheDataRepositoryAssociations:
    import aws_sdk_fsx.types.file_cache_data_repository_association

    out: CreateFileCacheDataRepositoryAssociations = []
    for item in data:
        out.append(
            aws_sdk_fsx.types.file_cache_data_repository_association.deserialize_aws_json_1_1(
                item
            )
        )
    return out
