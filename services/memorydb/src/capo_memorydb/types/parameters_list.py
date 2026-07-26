"""Generated from Smithy shape ``com.amazonaws.memorydb#ParametersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_memorydb.types.parameter

ParametersList: TypeAlias = list["capo_memorydb.types.parameter.Parameter"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParametersList) -> list:
    import capo_memorydb.types.parameter

    out: list = []
    for item in value:
        out.append(capo_memorydb.types.parameter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ParametersList:
    import capo_memorydb.types.parameter

    out: ParametersList = []
    for item in data:
        out.append(capo_memorydb.types.parameter.deserialize_aws_json_1_1(item))
    return out
