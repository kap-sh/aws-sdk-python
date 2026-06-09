"""Generated from Smithy shape ``com.amazonaws.dynamodb#CancellationReason``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.attribute_map
    import aws_sdk_dynamodb.types.code
    import aws_sdk_dynamodb.types.error_message


class CancellationReason(TypedDict):
    item: NotRequired["aws_sdk_dynamodb.types.attribute_map.AttributeMap"]
    """<p>Item in the request which caused the transaction to get cancelled.</p>"""
    code: NotRequired["aws_sdk_dynamodb.types.code.Code"]
    """<p>Status code for the result of the cancelled transaction.</p>"""
    message: NotRequired["aws_sdk_dynamodb.types.error_message.ErrorMessage"]
    """<p>Cancellation reason message description.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CancellationReason) -> dict:
    out: dict = {}
    if "item" in value:
        import aws_sdk_dynamodb.types.attribute_map

        out["Item"] = aws_sdk_dynamodb.types.attribute_map.serialize_aws_json_1_0(
            value["item"]
        )
    if "code" in value:
        out["Code"] = value["code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CancellationReason:
    out: CancellationReason = {}  # type: ignore[typeddict-item]
    if "Item" in data:
        import aws_sdk_dynamodb.types.attribute_map

        out["item"] = aws_sdk_dynamodb.types.attribute_map.deserialize_aws_json_1_0(
            data["Item"]
        )
    if "Code" in data:
        out["code"] = data["Code"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out
