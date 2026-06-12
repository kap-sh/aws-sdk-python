"""Generated from Smithy shape ``com.amazonaws.kendra#DataSourceGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.data_source_group

DataSourceGroups: TypeAlias = list[
    "aws_sdk_kendra.types.data_source_group.DataSourceGroup"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataSourceGroups) -> list:
    import aws_sdk_kendra.types.data_source_group

    out: list = []
    for item in value:
        out.append(aws_sdk_kendra.types.data_source_group.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DataSourceGroups:
    import aws_sdk_kendra.types.data_source_group

    out: DataSourceGroups = []
    for item in data:
        out.append(
            aws_sdk_kendra.types.data_source_group.deserialize_aws_json_1_1(item)
        )
    return out
