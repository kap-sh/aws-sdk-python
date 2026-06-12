"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsSnsTopicSubscription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsSnsTopicSubscription(TypedDict):
    endpoint: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The subscription's endpoint (format depends on the protocol).</p>"""
    protocol: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The subscription's protocol.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsSnsTopicSubscription) -> dict:
    out: dict = {}
    if "endpoint" in value:
        out["Endpoint"] = value["endpoint"]
    if "protocol" in value:
        out["Protocol"] = value["protocol"]
    return out


def deserialize_json(data: dict) -> AwsSnsTopicSubscription:
    out: AwsSnsTopicSubscription = {}  # type: ignore[typeddict-item]
    if "Endpoint" in data:
        out["endpoint"] = data["Endpoint"]
    if "Protocol" in data:
        out["protocol"] = data["Protocol"]
    return out
