"""Generated from Smithy shape ``com.amazonaws.devicefarm#UniqueProblemsByExecutionResultMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_device_farm.types.execution_result
    import capo_device_farm.types.unique_problems

UniqueProblemsByExecutionResultMap: TypeAlias = dict[
    "capo_device_farm.types.execution_result.ExecutionResult",
    "capo_device_farm.types.unique_problems.UniqueProblems",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    input_to_serialize: UniqueProblemsByExecutionResultMap,
) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_device_farm.types.execution_result
        import capo_device_farm.types.unique_problems

        out[capo_device_farm.types.execution_result.serialize_aws_json_1_1(key)] = (
            capo_device_farm.types.unique_problems.serialize_aws_json_1_1(value)
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UniqueProblemsByExecutionResultMap:
    out: UniqueProblemsByExecutionResultMap = {}
    for key, value in data.items():
        import capo_device_farm.types.execution_result
        import capo_device_farm.types.unique_problems

        out[capo_device_farm.types.execution_result.deserialize_aws_json_1_1(key)] = (
            capo_device_farm.types.unique_problems.deserialize_aws_json_1_1(value)
        )
    return out
