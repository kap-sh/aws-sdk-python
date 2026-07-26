"""Generated from Smithy shape ``com.amazonaws.mq#UpdateConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mq.types.__string


class UpdateConfigurationRequest(TypedDict, closed=True):
    configuration_id: "capo_mq.types.__string.__string"
    """<p>The unique ID that Amazon MQ generates for the configuration.</p>"""
    data: NotRequired["capo_mq.types.__string.__string"]
    """<p>Amazon MQ for Active MQ: The base64-encoded XML configuration. Amazon MQ for RabbitMQ: the base64-encoded Cuttlefish configuration.</p>"""
    description: NotRequired["capo_mq.types.__string.__string"]
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
