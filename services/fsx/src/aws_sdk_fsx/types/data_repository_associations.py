"""Generated from Smithy shape ``com.amazonaws.fsx#DataRepositoryAssociations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fsx.types.data_repository_association

DataRepositoryAssociations: TypeAlias = list[
    "aws_sdk_fsx.types.data_repository_association.DataRepositoryAssociation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataRepositoryAssociations) -> list:
    import aws_sdk_fsx.types.data_repository_association

    out: list = []
    for item in value:
        out.append(
            aws_sdk_fsx.types.data_repository_association.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DataRepositoryAssociations:
    import aws_sdk_fsx.types.data_repository_association

    out: DataRepositoryAssociations = []
    for item in data:
        out.append(
            aws_sdk_fsx.types.data_repository_association.deserialize_aws_json_1_1(item)
        )
    return out
