"""Generated from Smithy shape ``com.amazonaws.greengrass#Subscription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.__string


class Subscription(TypedDict, closed=True):
    id: NotRequired["capo_greengrass.types.__string.__string"]
    """A descriptive or arbitrary ID for the subscription. This value must be unique within the subscription definition version. Max length is 128 characters with pattern ''[a-zA-Z0-9:_-]+''."""
    source: NotRequired["capo_greengrass.types.__string.__string"]
    """The source of the subscription. Can be a thing ARN, a Lambda function ARN, a connector ARN, 'cloud' (which represents the AWS IoT cloud), or 'GGShadowService'."""
    subject: NotRequired["capo_greengrass.types.__string.__string"]
    """The MQTT topic used to route the message."""
    target: NotRequired["capo_greengrass.types.__string.__string"]
    """Where the message is sent to. Can be a thing ARN, a Lambda function ARN, a connector ARN, 'cloud' (which represents the AWS IoT cloud), or 'GGShadowService'."""


# --- restJson1 ser/de ---
def serialize_json(value: Subscription) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "source" in value:
        out["Source"] = value["source"]
    if "subject" in value:
        out["Subject"] = value["subject"]
    if "target" in value:
        out["Target"] = value["target"]
    return out


def deserialize_json(data: dict) -> Subscription:
    out: Subscription = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Source" in data:
        out["source"] = data["Source"]
    if "Subject" in data:
        out["subject"] = data["Subject"]
    if "Target" in data:
        out["target"] = data["Target"]
    return out
