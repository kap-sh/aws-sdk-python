"""Generated from Smithy shape ``com.amazonaws.personalize#ExcludedDatasetColumns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_personalize.types.column_names_list
    import aws_sdk_personalize.types.dataset_type

ExcludedDatasetColumns: TypeAlias = dict[
    "aws_sdk_personalize.types.dataset_type.DatasetType",
    "aws_sdk_personalize.types.column_names_list.ColumnNamesList",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ExcludedDatasetColumns) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_personalize.types.column_names_list

        out[key] = aws_sdk_personalize.types.column_names_list.serialize_aws_json_1_1(
            value
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExcludedDatasetColumns:
    out: ExcludedDatasetColumns = {}
    for key, value in data.items():
        import aws_sdk_personalize.types.column_names_list

        out[key] = aws_sdk_personalize.types.column_names_list.deserialize_aws_json_1_1(
            value
        )
    return out
