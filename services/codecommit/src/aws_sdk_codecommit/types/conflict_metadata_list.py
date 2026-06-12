"""Generated from Smithy shape ``com.amazonaws.codecommit#ConflictMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.conflict_metadata

ConflictMetadataList: TypeAlias = list[
    "aws_sdk_codecommit.types.conflict_metadata.ConflictMetadata"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConflictMetadataList) -> list:
    import aws_sdk_codecommit.types.conflict_metadata

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codecommit.types.conflict_metadata.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConflictMetadataList:
    import aws_sdk_codecommit.types.conflict_metadata

    out: ConflictMetadataList = []
    for item in data:
        out.append(
            aws_sdk_codecommit.types.conflict_metadata.deserialize_aws_json_1_1(item)
        )
    return out
