"""Generated from Smithy shape ``com.amazonaws.quicksight#Datasets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.dataset_metadata

Datasets: TypeAlias = list["aws_sdk_quicksight.types.dataset_metadata.DatasetMetadata"]


# --- restJson1 ser/de ---
def serialize_json(value: Datasets) -> list:
    import aws_sdk_quicksight.types.dataset_metadata

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.dataset_metadata.serialize_json(item))
    return out


def deserialize_json(data: list) -> Datasets:
    import aws_sdk_quicksight.types.dataset_metadata

    out: Datasets = []
    for item in data:
        out.append(aws_sdk_quicksight.types.dataset_metadata.deserialize_json(item))
    return out
