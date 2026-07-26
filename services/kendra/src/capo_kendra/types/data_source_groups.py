"""Generated from Smithy shape ``com.amazonaws.kendra#DataSourceGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.data_source_group

DataSourceGroups: TypeAlias = list[
    "capo_kendra.types.data_source_group.DataSourceGroup"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataSourceGroups) -> list:
    import capo_kendra.types.data_source_group

    out: list = []
    for item in value:
        out.append(capo_kendra.types.data_source_group.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DataSourceGroups:
    import capo_kendra.types.data_source_group

    out: DataSourceGroups = []
    for item in data:
        out.append(capo_kendra.types.data_source_group.deserialize_aws_json_1_1(item))
    return out
