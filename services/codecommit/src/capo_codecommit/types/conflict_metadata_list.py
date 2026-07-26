"""Generated from Smithy shape ``com.amazonaws.codecommit#ConflictMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codecommit.types.conflict_metadata

ConflictMetadataList: TypeAlias = list[
    "capo_codecommit.types.conflict_metadata.ConflictMetadata"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConflictMetadataList) -> list:
    import capo_codecommit.types.conflict_metadata

    out: list = []
    for item in value:
        out.append(capo_codecommit.types.conflict_metadata.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ConflictMetadataList:
    import capo_codecommit.types.conflict_metadata

    out: ConflictMetadataList = []
    for item in data:
        out.append(
            capo_codecommit.types.conflict_metadata.deserialize_aws_json_1_1(item)
        )
    return out
