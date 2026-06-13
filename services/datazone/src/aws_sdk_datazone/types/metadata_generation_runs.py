"""Generated from Smithy shape ``com.amazonaws.datazone#MetadataGenerationRuns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.metadata_generation_run_item

MetadataGenerationRuns: TypeAlias = list[
    "aws_sdk_datazone.types.metadata_generation_run_item.MetadataGenerationRunItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetadataGenerationRuns) -> list:
    import aws_sdk_datazone.types.metadata_generation_run_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_datazone.types.metadata_generation_run_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> MetadataGenerationRuns:
    import aws_sdk_datazone.types.metadata_generation_run_item

    out: MetadataGenerationRuns = []
    for item in data:
        out.append(
            aws_sdk_datazone.types.metadata_generation_run_item.deserialize_json(item)
        )
    return out
