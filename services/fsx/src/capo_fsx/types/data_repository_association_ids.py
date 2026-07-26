"""Generated from Smithy shape ``com.amazonaws.fsx#DataRepositoryAssociationIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fsx.types.data_repository_association_id

DataRepositoryAssociationIds: TypeAlias = list[
    "capo_fsx.types.data_repository_association_id.DataRepositoryAssociationId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataRepositoryAssociationIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DataRepositoryAssociationIds:
    return list(data)
