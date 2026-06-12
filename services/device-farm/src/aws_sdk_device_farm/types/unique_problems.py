"""Generated from Smithy shape ``com.amazonaws.devicefarm#UniqueProblems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.unique_problem

UniqueProblems: TypeAlias = list[
    "aws_sdk_device_farm.types.unique_problem.UniqueProblem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UniqueProblems) -> list:
    import aws_sdk_device_farm.types.unique_problem

    out: list = []
    for item in value:
        out.append(
            aws_sdk_device_farm.types.unique_problem.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UniqueProblems:
    import aws_sdk_device_farm.types.unique_problem

    out: UniqueProblems = []
    for item in data:
        out.append(
            aws_sdk_device_farm.types.unique_problem.deserialize_aws_json_1_1(item)
        )
    return out
