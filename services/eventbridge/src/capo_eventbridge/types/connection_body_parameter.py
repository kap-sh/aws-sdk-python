"""Generated from Smithy shape ``com.amazonaws.eventbridge#ConnectionBodyParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.boolean
    import capo_eventbridge.types.sensitive_string
    import capo_eventbridge.types.string


class ConnectionBodyParameter(TypedDict, closed=True):
    key: NotRequired["capo_eventbridge.types.string.String"]
    """<p>The key for the parameter.</p>"""
    value: NotRequired["capo_eventbridge.types.sensitive_string.SensitiveString"]
    """<p>The value associated with the key.</p>"""
    is_value_secret: "capo_eventbridge.types.boolean.Boolean"
    """<p>Specifies whether the value is secret.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionBodyParameter) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    out["IsValueSecret"] = value.get("is_value_secret", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectionBodyParameter:
    out: ConnectionBodyParameter = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    if "Value" in data:
        out["value"] = data["Value"]
    if "IsValueSecret" in data:
        out["is_value_secret"] = data["IsValueSecret"]
    else:
        out["is_value_secret"] = False
    return out
