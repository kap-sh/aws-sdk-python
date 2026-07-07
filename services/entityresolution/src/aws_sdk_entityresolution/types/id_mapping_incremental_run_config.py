"""Generated from Smithy shape ``com.amazonaws.entityresolution#IdMappingIncrementalRunConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.id_mapping_incremental_run_type


class IdMappingIncrementalRunConfig(TypedDict, closed=True):
    incremental_run_type: NotRequired[
        "aws_sdk_entityresolution.types.id_mapping_incremental_run_type.IdMappingIncrementalRunType"
    ]
    """<p> The incremental run type for an ID mapping workflow.</p> <p>It takes only one value: <code>ON_DEMAND</code>. This setting runs the ID mapping workflow when it's manually triggered through the <code>StartIdMappingJob</code> API.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdMappingIncrementalRunConfig) -> dict:
    out: dict = {}
    if "incremental_run_type" in value:
        import aws_sdk_entityresolution.types.id_mapping_incremental_run_type

        out["incrementalRunType"] = (
            aws_sdk_entityresolution.types.id_mapping_incremental_run_type.serialize_json(
                value["incremental_run_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> IdMappingIncrementalRunConfig:
    out: IdMappingIncrementalRunConfig = {}  # type: ignore[typeddict-item]
    if "incrementalRunType" in data:
        import aws_sdk_entityresolution.types.id_mapping_incremental_run_type

        out["incremental_run_type"] = (
            aws_sdk_entityresolution.types.id_mapping_incremental_run_type.deserialize_json(
                data["incrementalRunType"]
            )
        )
    return out
