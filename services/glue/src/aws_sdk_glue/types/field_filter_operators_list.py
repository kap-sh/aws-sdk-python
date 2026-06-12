"""Generated from Smithy shape ``com.amazonaws.glue#FieldFilterOperatorsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.field_filter_operator

FieldFilterOperatorsList: TypeAlias = list[
    "aws_sdk_glue.types.field_filter_operator.FieldFilterOperator"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FieldFilterOperatorsList) -> list:
    import aws_sdk_glue.types.field_filter_operator

    out: list = []
    for item in value:
        out.append(
            aws_sdk_glue.types.field_filter_operator.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FieldFilterOperatorsList:
    import aws_sdk_glue.types.field_filter_operator

    out: FieldFilterOperatorsList = []
    for item in data:
        out.append(
            aws_sdk_glue.types.field_filter_operator.deserialize_aws_json_1_1(item)
        )
    return out
