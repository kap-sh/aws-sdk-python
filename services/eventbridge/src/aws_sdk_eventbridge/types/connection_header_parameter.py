"""Generated from Smithy shape ``com.amazonaws.eventbridge#ConnectionHeaderParameter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.boolean
    import aws_sdk_eventbridge.types.header_key
    import aws_sdk_eventbridge.types.header_value_sensitive


class ConnectionHeaderParameter(TypedDict):
    key: NotRequired["aws_sdk_eventbridge.types.header_key.HeaderKey"]
    """<p>The key for the parameter.</p>"""
    value: NotRequired[
        "aws_sdk_eventbridge.types.header_value_sensitive.HeaderValueSensitive"
    ]
    """<p>The value associated with the key.</p>"""
    is_value_secret: "aws_sdk_eventbridge.types.boolean.Boolean"
    """<p>Specifies whether the value is a secret.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionHeaderParameter) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    out["IsValueSecret"] = value.get("is_value_secret", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectionHeaderParameter:
    out: ConnectionHeaderParameter = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    if "Value" in data:
        out["value"] = data["Value"]
    if "IsValueSecret" in data:
        out["is_value_secret"] = data["IsValueSecret"]
    else:
        out["is_value_secret"] = False
    return out
