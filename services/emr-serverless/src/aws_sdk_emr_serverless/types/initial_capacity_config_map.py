"""Generated from Smithy shape ``com.amazonaws.emrserverless#InitialCapacityConfigMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.initial_capacity_config
    import aws_sdk_emr_serverless.types.worker_type_string

InitialCapacityConfigMap: TypeAlias = dict[
    "aws_sdk_emr_serverless.types.worker_type_string.WorkerTypeString",
    "aws_sdk_emr_serverless.types.initial_capacity_config.InitialCapacityConfig",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: InitialCapacityConfigMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_emr_serverless.types.initial_capacity_config

        out[key] = aws_sdk_emr_serverless.types.initial_capacity_config.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> InitialCapacityConfigMap:
    out: InitialCapacityConfigMap = {}
    for key, value in data.items():
        import aws_sdk_emr_serverless.types.initial_capacity_config

        out[key] = (
            aws_sdk_emr_serverless.types.initial_capacity_config.deserialize_json(value)
        )
    return out
