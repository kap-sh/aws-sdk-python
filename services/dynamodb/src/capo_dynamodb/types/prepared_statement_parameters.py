"""Generated from Smithy shape ``com.amazonaws.dynamodb#PreparedStatementParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.attribute_value

PreparedStatementParameters: TypeAlias = list[
    "capo_dynamodb.types.attribute_value.AttributeValue"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PreparedStatementParameters) -> list:
    import capo_dynamodb.types.attribute_value

    out: list = []
    for item in value:
        out.append(capo_dynamodb.types.attribute_value.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> PreparedStatementParameters:
    import capo_dynamodb.types.attribute_value

    out: PreparedStatementParameters = []
    for item in data:
        if item is None:
            continue
        out.append(capo_dynamodb.types.attribute_value.deserialize_aws_json_1_0(item))
    return out
