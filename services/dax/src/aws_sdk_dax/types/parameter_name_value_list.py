"""Generated from Smithy shape ``com.amazonaws.dax#ParameterNameValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dax.types.parameter_name_value

ParameterNameValueList: TypeAlias = list[
    "aws_sdk_dax.types.parameter_name_value.ParameterNameValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterNameValueList) -> list:
    import aws_sdk_dax.types.parameter_name_value

    out: list = []
    for item in value:
        out.append(aws_sdk_dax.types.parameter_name_value.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ParameterNameValueList:
    import aws_sdk_dax.types.parameter_name_value

    out: ParameterNameValueList = []
    for item in data:
        out.append(
            aws_sdk_dax.types.parameter_name_value.deserialize_aws_json_1_1(item)
        )
    return out
