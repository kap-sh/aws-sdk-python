"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#EvaluationErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.evaluation_error_item

EvaluationErrorList: TypeAlias = list[
    "aws_sdk_verifiedpermissions.types.evaluation_error_item.EvaluationErrorItem"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EvaluationErrorList) -> list:
    import aws_sdk_verifiedpermissions.types.evaluation_error_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_verifiedpermissions.types.evaluation_error_item.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> EvaluationErrorList:
    import aws_sdk_verifiedpermissions.types.evaluation_error_item

    out: EvaluationErrorList = []
    for item in data:
        out.append(
            aws_sdk_verifiedpermissions.types.evaluation_error_item.deserialize_aws_json_1_0(
                item
            )
        )
    return out
