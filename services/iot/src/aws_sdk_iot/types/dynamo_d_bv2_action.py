"""Generated from Smithy shape ``com.amazonaws.iot#DynamoDBv2Action``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.aws_arn
    import aws_sdk_iot.types.put_item_input


class DynamoDBv2Action(TypedDict):
    role_arn: "aws_sdk_iot.types.aws_arn.AwsArn"
    """<p>The ARN of the IAM role that grants access to the DynamoDB table.</p>"""
    put_item: "aws_sdk_iot.types.put_item_input.PutItemInput"
    r"""<p>Specifies the DynamoDB table to which the message data will be written. For example:</p> <p> <code>{ \"dynamoDBv2\": { \"roleArn\": \"aws:iam:12341251:my-role\" \"putItem\": { \"tableName\": \"my-table\" } } }</code> </p> <p>Each attribute in the message payload will be written to a separate column in the DynamoDB database.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DynamoDBv2Action) -> dict:
    out: dict = {}
    out["roleArn"] = value["role_arn"]
    import aws_sdk_iot.types.put_item_input

    out["putItem"] = aws_sdk_iot.types.put_item_input.serialize_json(value["put_item"])
    return out


def deserialize_json(data: dict) -> DynamoDBv2Action:
    out: DynamoDBv2Action = {}  # type: ignore[typeddict-item]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("DynamoDBv2Action.role_arn required")
    if "putItem" in data:
        import aws_sdk_iot.types.put_item_input

        out["put_item"] = aws_sdk_iot.types.put_item_input.deserialize_json(
            data["putItem"]
        )
    else:
        raise DeserializationError("DynamoDBv2Action.put_item required")
    return out
