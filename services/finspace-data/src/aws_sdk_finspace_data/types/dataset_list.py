"""Generated from Smithy shape ``com.amazonaws.finspacedata#DatasetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.dataset

DatasetList: TypeAlias = list["aws_sdk_finspace_data.types.dataset.Dataset"]


# --- restJson1 ser/de ---
def serialize_json(value: DatasetList) -> list:
    import aws_sdk_finspace_data.types.dataset

    out: list = []
    for item in value:
        out.append(aws_sdk_finspace_data.types.dataset.serialize_json(item))
    return out


def deserialize_json(data: list) -> DatasetList:
    import aws_sdk_finspace_data.types.dataset

    out: DatasetList = []
    for item in data:
        out.append(aws_sdk_finspace_data.types.dataset.deserialize_json(item))
    return out
