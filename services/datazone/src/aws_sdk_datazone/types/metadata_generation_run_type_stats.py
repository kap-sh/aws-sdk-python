"""Generated from Smithy shape ``com.amazonaws.datazone#MetadataGenerationRunTypeStats``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.metadata_generation_run_type_stat

MetadataGenerationRunTypeStats: TypeAlias = list[
    "aws_sdk_datazone.types.metadata_generation_run_type_stat.MetadataGenerationRunTypeStat"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetadataGenerationRunTypeStats) -> list:
    import aws_sdk_datazone.types.metadata_generation_run_type_stat

    out: list = []
    for item in value:
        out.append(
            aws_sdk_datazone.types.metadata_generation_run_type_stat.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MetadataGenerationRunTypeStats:
    import aws_sdk_datazone.types.metadata_generation_run_type_stat

    out: MetadataGenerationRunTypeStats = []
    for item in data:
        out.append(
            aws_sdk_datazone.types.metadata_generation_run_type_stat.deserialize_json(
                item
            )
        )
    return out
