"""Generated from Smithy shape ``com.amazonaws.qbusiness#DataSources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.data_source

DataSources: TypeAlias = list["aws_sdk_qbusiness.types.data_source.DataSource"]


# --- restJson1 ser/de ---
def serialize_json(value: DataSources) -> list:
    import aws_sdk_qbusiness.types.data_source

    out: list = []
    for item in value:
        out.append(aws_sdk_qbusiness.types.data_source.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataSources:
    import aws_sdk_qbusiness.types.data_source

    out: DataSources = []
    for item in data:
        out.append(aws_sdk_qbusiness.types.data_source.deserialize_json(item))
    return out
