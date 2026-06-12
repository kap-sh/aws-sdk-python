"""Generated from Smithy shape ``com.amazonaws.emrserverless#LogTypeMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.log_type_list
    import aws_sdk_emr_serverless.types.worker_type_string

LogTypeMap: TypeAlias = dict[
    "aws_sdk_emr_serverless.types.worker_type_string.WorkerTypeString",
    "aws_sdk_emr_serverless.types.log_type_list.LogTypeList",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: LogTypeMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_emr_serverless.types.log_type_list

        out[key] = aws_sdk_emr_serverless.types.log_type_list.serialize_json(value)
    return out


def deserialize_json(data: dict) -> LogTypeMap:
    out: LogTypeMap = {}
    for key, value in data.items():
        import aws_sdk_emr_serverless.types.log_type_list

        out[key] = aws_sdk_emr_serverless.types.log_type_list.deserialize_json(value)
    return out
