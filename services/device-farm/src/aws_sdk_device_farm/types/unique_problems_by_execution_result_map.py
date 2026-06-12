"""Generated from Smithy shape ``com.amazonaws.devicefarm#UniqueProblemsByExecutionResultMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.execution_result
    import aws_sdk_device_farm.types.unique_problems

UniqueProblemsByExecutionResultMap: TypeAlias = dict[
    "aws_sdk_device_farm.types.execution_result.ExecutionResult",
    "aws_sdk_device_farm.types.unique_problems.UniqueProblems",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    input_to_serialize: UniqueProblemsByExecutionResultMap,
) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_device_farm.types.execution_result
        import aws_sdk_device_farm.types.unique_problems

        out[aws_sdk_device_farm.types.execution_result.serialize_aws_json_1_1(key)] = (
            aws_sdk_device_farm.types.unique_problems.serialize_aws_json_1_1(value)
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UniqueProblemsByExecutionResultMap:
    out: UniqueProblemsByExecutionResultMap = {}
    for key, value in data.items():
        import aws_sdk_device_farm.types.execution_result
        import aws_sdk_device_farm.types.unique_problems

        out[
            aws_sdk_device_farm.types.execution_result.deserialize_aws_json_1_1(key)
        ] = aws_sdk_device_farm.types.unique_problems.deserialize_aws_json_1_1(value)
    return out
