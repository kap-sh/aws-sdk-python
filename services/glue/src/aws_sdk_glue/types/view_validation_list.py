"""Generated from Smithy shape ``com.amazonaws.glue#ViewValidationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.view_validation

ViewValidationList: TypeAlias = list[
    "aws_sdk_glue.types.view_validation.ViewValidation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ViewValidationList) -> list:
    import aws_sdk_glue.types.view_validation

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.view_validation.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ViewValidationList:
    import aws_sdk_glue.types.view_validation

    out: ViewValidationList = []
    for item in data:
        out.append(aws_sdk_glue.types.view_validation.deserialize_aws_json_1_1(item))
    return out
