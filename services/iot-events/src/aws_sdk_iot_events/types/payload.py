"""Generated from Smithy shape ``com.amazonaws.iotevents#Payload``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot_events.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.content_expression
    import aws_sdk_iot_events.types.payload_type


class Payload(TypedDict):
    content_expression: "aws_sdk_iot_events.types.content_expression.ContentExpression"
    """<p>The content of the payload. You can use a string expression that includes quoted strings (<code>'<string>'</code>), variables (<code>$variable.<variable-name></code>), input values (<code>$input.<input-name>.<path-to-datum></code>), string concatenations, and quoted strings that contain <code>${}</code> as the content. The recommended maximum size of a content expression is 1 KB.</p>"""
    type: "aws_sdk_iot_events.types.payload_type.PayloadType"
    """<p>The value of the payload type can be either <code>STRING</code> or <code>JSON</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Payload) -> dict:
    out: dict = {}
    out["contentExpression"] = value["content_expression"]
    import aws_sdk_iot_events.types.payload_type

    out["type"] = aws_sdk_iot_events.types.payload_type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> Payload:
    out: Payload = {}  # type: ignore[typeddict-item]
    if "contentExpression" in data:
        out["content_expression"] = data["contentExpression"]
    else:
        raise DeserializationError("Payload.content_expression required")
    if "type" in data:
        import aws_sdk_iot_events.types.payload_type

        out["type"] = aws_sdk_iot_events.types.payload_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("Payload.type required")
    return out
