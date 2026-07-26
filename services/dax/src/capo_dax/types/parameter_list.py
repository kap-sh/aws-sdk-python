"""Generated from Smithy shape ``com.amazonaws.dax#ParameterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dax.types.parameter

ParameterList: TypeAlias = list["capo_dax.types.parameter.Parameter"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterList) -> list:
    import capo_dax.types.parameter

    out: list = []
    for item in value:
        out.append(capo_dax.types.parameter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ParameterList:
    import capo_dax.types.parameter

    out: ParameterList = []
    for item in data:
        out.append(capo_dax.types.parameter.deserialize_aws_json_1_1(item))
    return out
