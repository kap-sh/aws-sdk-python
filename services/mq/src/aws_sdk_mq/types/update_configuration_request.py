"""Generated from Smithy shape ``com.amazonaws.mq#UpdateConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mq.types.__string


class UpdateConfigurationRequest(TypedDict):
    configuration_id: "aws_sdk_mq.types.__string.__string"
    """<p>The unique ID that Amazon MQ generates for the configuration.</p>"""
    data: NotRequired["aws_sdk_mq.types.__string.__string"]
    """<p>Amazon MQ for Active MQ: The base64-encoded XML configuration. Amazon MQ for RabbitMQ: the base64-encoded Cuttlefish configuration.</p>"""
    description: NotRequired["aws_sdk_mq.types.__string.__string"]
    """<p>The description of the configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConfigurationRequest) -> dict:
    out: dict = {}
    if "data" in value:
        out["data"] = value["data"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateConfigurationRequest:
    out: UpdateConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "data" in data:
        out["data"] = data["data"]
    if "description" in data:
        out["description"] = data["description"]
    return out
