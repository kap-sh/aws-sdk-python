"""Generated from Smithy shape ``com.amazonaws.glue#OrchestrationArgumentsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.orchestration_arguments_value
    import aws_sdk_glue.types.orchestration_name_string

OrchestrationArgumentsMap: TypeAlias = dict[
    "aws_sdk_glue.types.orchestration_name_string.OrchestrationNameString",
    "aws_sdk_glue.types.orchestration_arguments_value.OrchestrationArgumentsValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: OrchestrationArgumentsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> OrchestrationArgumentsMap:
    out: OrchestrationArgumentsMap = {}
    for key, value in data.items():
        out[key] = value
    return out
