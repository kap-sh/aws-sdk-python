"""Generated from Smithy shape ``com.amazonaws.machinelearning#DataSources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_machine_learning.types.data_source

DataSources: TypeAlias = list["capo_machine_learning.types.data_source.DataSource"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataSources) -> list:
    import capo_machine_learning.types.data_source

    out: list = []
    for item in value:
        out.append(capo_machine_learning.types.data_source.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DataSources:
    import capo_machine_learning.types.data_source

    out: DataSources = []
    for item in data:
        out.append(
            capo_machine_learning.types.data_source.deserialize_aws_json_1_1(item)
        )
    return out
