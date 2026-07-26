"""Generated from Smithy shape ``com.amazonaws.glue#TransformConfigParameterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.transform_config_parameter

TransformConfigParameterList: TypeAlias = list[
    "capo_glue.types.transform_config_parameter.TransformConfigParameter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TransformConfigParameterList) -> list:
    import capo_glue.types.transform_config_parameter

    out: list = []
    for item in value:
        out.append(
            capo_glue.types.transform_config_parameter.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TransformConfigParameterList:
    import capo_glue.types.transform_config_parameter

    out: TransformConfigParameterList = []
    for item in data:
        out.append(
            capo_glue.types.transform_config_parameter.deserialize_aws_json_1_1(item)
        )
    return out
