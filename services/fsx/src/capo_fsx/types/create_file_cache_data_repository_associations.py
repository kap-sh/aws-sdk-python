"""Generated from Smithy shape ``com.amazonaws.fsx#CreateFileCacheDataRepositoryAssociations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fsx.types.file_cache_data_repository_association

CreateFileCacheDataRepositoryAssociations: TypeAlias = list[
    "capo_fsx.types.file_cache_data_repository_association.FileCacheDataRepositoryAssociation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateFileCacheDataRepositoryAssociations) -> list:
    import capo_fsx.types.file_cache_data_repository_association

    out: list = []
    for item in value:
        out.append(
            capo_fsx.types.file_cache_data_repository_association.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CreateFileCacheDataRepositoryAssociations:
    import capo_fsx.types.file_cache_data_repository_association

    out: CreateFileCacheDataRepositoryAssociations = []
    for item in data:
        out.append(
            capo_fsx.types.file_cache_data_repository_association.deserialize_aws_json_1_1(
                item
            )
        )
    return out
