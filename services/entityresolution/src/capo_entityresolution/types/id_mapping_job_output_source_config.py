"""Generated from Smithy shape ``com.amazonaws.entityresolution#IdMappingJobOutputSourceConfig``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_entityresolution.types.id_mapping_job_output_source

IdMappingJobOutputSourceConfig: TypeAlias = list[
    "capo_entityresolution.types.id_mapping_job_output_source.IdMappingJobOutputSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: IdMappingJobOutputSourceConfig) -> list:
    import capo_entityresolution.types.id_mapping_job_output_source

    out: list = []
    for item in value:
        out.append(
            capo_entityresolution.types.id_mapping_job_output_source.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> IdMappingJobOutputSourceConfig:
    import capo_entityresolution.types.id_mapping_job_output_source

    out: IdMappingJobOutputSourceConfig = []
    for item in data:
        out.append(
            capo_entityresolution.types.id_mapping_job_output_source.deserialize_json(
                item
            )
        )
    return out
