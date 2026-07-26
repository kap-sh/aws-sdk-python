"""Generated from Smithy shape ``com.amazonaws.dynamodb#ParameterizedStatements``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.parameterized_statement

ParameterizedStatements: TypeAlias = list[
    "capo_dynamodb.types.parameterized_statement.ParameterizedStatement"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ParameterizedStatements) -> list:
    import capo_dynamodb.types.parameterized_statement

    out: list = []
    for item in value:
        out.append(
            capo_dynamodb.types.parameterized_statement.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ParameterizedStatements:
    import capo_dynamodb.types.parameterized_statement

    out: ParameterizedStatements = []
    for item in data:
        out.append(
            capo_dynamodb.types.parameterized_statement.deserialize_aws_json_1_0(item)
        )
    return out
