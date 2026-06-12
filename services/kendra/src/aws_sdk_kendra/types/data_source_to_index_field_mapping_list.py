"""Generated from Smithy shape ``com.amazonaws.kendra#DataSourceToIndexFieldMappingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.data_source_to_index_field_mapping

DataSourceToIndexFieldMappingList: TypeAlias = list[
    "aws_sdk_kendra.types.data_source_to_index_field_mapping.DataSourceToIndexFieldMapping"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataSourceToIndexFieldMappingList) -> list:
    import aws_sdk_kendra.types.data_source_to_index_field_mapping

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kendra.types.data_source_to_index_field_mapping.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DataSourceToIndexFieldMappingList:
    import aws_sdk_kendra.types.data_source_to_index_field_mapping

    out: DataSourceToIndexFieldMappingList = []
    for item in data:
        out.append(
            aws_sdk_kendra.types.data_source_to_index_field_mapping.deserialize_aws_json_1_1(
                item
            )
        )
    return out
