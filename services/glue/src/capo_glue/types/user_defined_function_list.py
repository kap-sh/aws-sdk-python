"""Generated from Smithy shape ``com.amazonaws.glue#UserDefinedFunctionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.user_defined_function

UserDefinedFunctionList: TypeAlias = list[
    "capo_glue.types.user_defined_function.UserDefinedFunction"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserDefinedFunctionList) -> list:
    import capo_glue.types.user_defined_function

    out: list = []
    for item in value:
        out.append(capo_glue.types.user_defined_function.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> UserDefinedFunctionList:
    import capo_glue.types.user_defined_function

    out: UserDefinedFunctionList = []
    for item in data:
        out.append(capo_glue.types.user_defined_function.deserialize_aws_json_1_1(item))
    return out
