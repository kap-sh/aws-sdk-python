"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsAmazonMqBrokerLogsPendingDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.boolean


class AwsAmazonMqBrokerLogsPendingDetails(TypedDict, closed=True):
    audit: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p> Activates audit logging. Every user management action made using JMX or the ActiveMQ Web Console is logged. Doesn't apply to RabbitMQ brokers. </p>"""
    general: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p> Activates general logging. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsAmazonMqBrokerLogsPendingDetails) -> dict:
    out: dict = {}
    if "audit" in value:
        out["Audit"] = value["audit"]
    if "general" in value:
        out["General"] = value["general"]
    return out


def deserialize_json(data: dict) -> AwsAmazonMqBrokerLogsPendingDetails:
    out: AwsAmazonMqBrokerLogsPendingDetails = {}  # type: ignore[typeddict-item]
    if "Audit" in data:
        out["audit"] = data["Audit"]
    if "General" in data:
        out["general"] = data["General"]
    return out
