"""Generated from Smithy shape ``com.amazonaws.dynamodb#ParameterizedStatements``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.parameterized_statement

ParameterizedStatements: TypeAlias = list[
    "aws_sdk_dynamodb.types.parameterized_statement.ParameterizedStatement"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ParameterizedStatements) -> list:
    import aws_sdk_dynamodb.types.parameterized_statement

    out: list = []
    for item in value:
        out.append(
            aws_sdk_dynamodb.types.parameterized_statement.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ParameterizedStatements:
    import aws_sdk_dynamodb.types.parameterized_statement

    out: ParameterizedStatements = []
    for item in data:
        out.append(
            aws_sdk_dynamodb.types.parameterized_statement.deserialize_aws_json_1_0(
                item
            )
        )
    return out
