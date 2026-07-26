"""Generated from Smithy shape ``com.amazonaws.codecommit#RepositoryMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codecommit.types.repository_metadata

RepositoryMetadataList: TypeAlias = list[
    "capo_codecommit.types.repository_metadata.RepositoryMetadata"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RepositoryMetadataList) -> list:
    import capo_codecommit.types.repository_metadata

    out: list = []
    for item in value:
        out.append(
            capo_codecommit.types.repository_metadata.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RepositoryMetadataList:
    import capo_codecommit.types.repository_metadata

    out: RepositoryMetadataList = []
    for item in data:
        out.append(
            capo_codecommit.types.repository_metadata.deserialize_aws_json_1_1(item)
        )
    return out
