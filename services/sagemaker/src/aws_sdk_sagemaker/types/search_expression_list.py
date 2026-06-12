"""Generated from Smithy shape ``com.amazonaws.sagemaker#SearchExpressionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.search_expression

SearchExpressionList: TypeAlias = list[
    "aws_sdk_sagemaker.types.search_expression.SearchExpression"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchExpressionList) -> list:
    import aws_sdk_sagemaker.types.search_expression

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.search_expression.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SearchExpressionList:
    import aws_sdk_sagemaker.types.search_expression

    out: SearchExpressionList = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.search_expression.deserialize_aws_json_1_1(item)
        )
    return out
