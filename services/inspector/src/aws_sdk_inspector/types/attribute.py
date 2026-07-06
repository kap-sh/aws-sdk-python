"""Generated from Smithy shape ``com.amazonaws.inspector#Attribute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector.types.attribute_key
    import aws_sdk_inspector.types.attribute_value


class Attribute(TypedDict, closed=True):
    key: "aws_sdk_inspector.types.attribute_key.AttributeKey"
    """<p>The attribute key.</p>"""
    value: NotRequired["aws_sdk_inspector.types.attribute_value.AttributeValue"]
    """<p>The value assigned to the attribute key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Attribute) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Attribute:
    out: Attribute = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("Attribute.key required")
    if "value" in data:
        out["value"] = data["value"]
    return out
