"""Generated from Smithy shape ``com.amazonaws.emrserverless#WorkerTypeSpecificationMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_emr_serverless.types.worker_type_specification
    import capo_emr_serverless.types.worker_type_string

WorkerTypeSpecificationMap: TypeAlias = dict[
    "capo_emr_serverless.types.worker_type_string.WorkerTypeString",
    "capo_emr_serverless.types.worker_type_specification.WorkerTypeSpecification",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: WorkerTypeSpecificationMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_emr_serverless.types.worker_type_specification

        out[key] = capo_emr_serverless.types.worker_type_specification.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> WorkerTypeSpecificationMap:
    out: WorkerTypeSpecificationMap = {}
    for key, value in data.items():
        import capo_emr_serverless.types.worker_type_specification

        out[key] = capo_emr_serverless.types.worker_type_specification.deserialize_json(
            value
        )
    return out
