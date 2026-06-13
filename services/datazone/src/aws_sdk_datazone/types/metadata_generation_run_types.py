"""Generated from Smithy shape ``com.amazonaws.datazone#MetadataGenerationRunTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.metadata_generation_run_type

MetadataGenerationRunTypes: TypeAlias = list[
    "aws_sdk_datazone.types.metadata_generation_run_type.MetadataGenerationRunType"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetadataGenerationRunTypes) -> list:
    import aws_sdk_datazone.types.metadata_generation_run_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_datazone.types.metadata_generation_run_type.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> MetadataGenerationRunTypes:
    import aws_sdk_datazone.types.metadata_generation_run_type

    out: MetadataGenerationRunTypes = []
    for item in data:
        out.append(
            aws_sdk_datazone.types.metadata_generation_run_type.deserialize_json(item)
        )
    return out
