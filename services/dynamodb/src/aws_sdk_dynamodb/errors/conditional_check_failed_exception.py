"""Generated from Smithy shape ``com.amazonaws.dynamodb#ConditionalCheckFailedException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.attribute_map
    import aws_sdk_dynamodb.types.error_message


class ConditionalCheckFailedException_(TypedDict):
    message: NotRequired["aws_sdk_dynamodb.types.error_message.ErrorMessage"]
    """<p>The conditional request failed.</p>"""
    item: NotRequired["aws_sdk_dynamodb.types.attribute_map.AttributeMap"]
    """<p>Item which caused the <code>ConditionalCheckFailedException</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConditionalCheckFailedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "item" in value:
        import aws_sdk_dynamodb.types.attribute_map

        out["Item"] = aws_sdk_dynamodb.types.attribute_map.serialize_aws_json_1_0(
            value["item"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ConditionalCheckFailedException_:
    out: ConditionalCheckFailedException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "Item" in data:
        import aws_sdk_dynamodb.types.attribute_map

        out["item"] = aws_sdk_dynamodb.types.attribute_map.deserialize_aws_json_1_0(
            data["Item"]
        )
    return out


class ConditionalCheckFailedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#ConditionalCheckFailedException``."""

    code: str | None = "ConditionalCheckFailedException"

    def __init__(self, data: ConditionalCheckFailedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConditionalCheckFailedException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "ConditionalCheckFailedException":
        return cls(deserialize_aws_json_1_0(data))
