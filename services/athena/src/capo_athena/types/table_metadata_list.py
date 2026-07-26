"""Generated from Smithy shape ``com.amazonaws.athena#TableMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_athena.types.table_metadata

TableMetadataList: TypeAlias = list["capo_athena.types.table_metadata.TableMetadata"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TableMetadataList) -> list:
    import capo_athena.types.table_metadata

    out: list = []
    for item in value:
        out.append(capo_athena.types.table_metadata.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TableMetadataList:
    import capo_athena.types.table_metadata

    out: TableMetadataList = []
    for item in data:
        out.append(capo_athena.types.table_metadata.deserialize_aws_json_1_1(item))
    return out
