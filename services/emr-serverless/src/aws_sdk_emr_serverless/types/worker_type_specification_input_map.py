"""Generated from Smithy shape ``com.amazonaws.emrserverless#WorkerTypeSpecificationInputMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.worker_type_specification_input
    import aws_sdk_emr_serverless.types.worker_type_string

WorkerTypeSpecificationInputMap: TypeAlias = dict[
    "aws_sdk_emr_serverless.types.worker_type_string.WorkerTypeString",
    "aws_sdk_emr_serverless.types.worker_type_specification_input.WorkerTypeSpecificationInput",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: WorkerTypeSpecificationInputMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_emr_serverless.types.worker_type_specification_input

        out[key] = (
            aws_sdk_emr_serverless.types.worker_type_specification_input.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> WorkerTypeSpecificationInputMap:
    out: WorkerTypeSpecificationInputMap = {}
    for key, value in data.items():
        import aws_sdk_emr_serverless.types.worker_type_specification_input

        out[key] = (
            aws_sdk_emr_serverless.types.worker_type_specification_input.deserialize_json(
                value
            )
        )
    return out
