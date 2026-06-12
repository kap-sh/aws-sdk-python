"""Generated from Smithy shape ``com.amazonaws.glue#UserDefinedFunctionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.user_defined_function

UserDefinedFunctionList: TypeAlias = list[
    "aws_sdk_glue.types.user_defined_function.UserDefinedFunction"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserDefinedFunctionList) -> list:
    import aws_sdk_glue.types.user_defined_function

    out: list = []
    for item in value:
        out.append(
            aws_sdk_glue.types.user_defined_function.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UserDefinedFunctionList:
    import aws_sdk_glue.types.user_defined_function

    out: UserDefinedFunctionList = []
    for item in data:
        out.append(
            aws_sdk_glue.types.user_defined_function.deserialize_aws_json_1_1(item)
        )
    return out
