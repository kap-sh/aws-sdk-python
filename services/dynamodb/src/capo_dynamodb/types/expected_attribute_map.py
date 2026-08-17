"""Generated from Smithy shape ``com.amazonaws.dynamodb#ExpectedAttributeMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.attribute_name
    import capo_dynamodb.types.expected_attribute_value

ExpectedAttributeMap: TypeAlias = dict[
    "capo_dynamodb.types.attribute_name.AttributeName",
    "capo_dynamodb.types.expected_attribute_value.ExpectedAttributeValue",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: ExpectedAttributeMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_dynamodb.types.expected_attribute_value

        out[key] = capo_dynamodb.types.expected_attribute_value.serialize_aws_json_1_0(
            value
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ExpectedAttributeMap:
    out: ExpectedAttributeMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_dynamodb.types.expected_attribute_value

        out[key] = (
            capo_dynamodb.types.expected_attribute_value.deserialize_aws_json_1_0(value)
        )
    return out
