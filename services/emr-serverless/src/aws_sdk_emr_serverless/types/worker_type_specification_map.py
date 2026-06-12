"""Generated from Smithy shape ``com.amazonaws.emrserverless#WorkerTypeSpecificationMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.worker_type_specification
    import aws_sdk_emr_serverless.types.worker_type_string

WorkerTypeSpecificationMap: TypeAlias = dict[
    "aws_sdk_emr_serverless.types.worker_type_string.WorkerTypeString",
    "aws_sdk_emr_serverless.types.worker_type_specification.WorkerTypeSpecification",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: WorkerTypeSpecificationMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_emr_serverless.types.worker_type_specification

        out[key] = (
            aws_sdk_emr_serverless.types.worker_type_specification.serialize_json(value)
        )
    return out


def deserialize_json(data: dict) -> WorkerTypeSpecificationMap:
    out: WorkerTypeSpecificationMap = {}
    for key, value in data.items():
        import aws_sdk_emr_serverless.types.worker_type_specification

        out[key] = (
            aws_sdk_emr_serverless.types.worker_type_specification.deserialize_json(
                value
            )
        )
    return out
