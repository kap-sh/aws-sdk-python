"""Generated from Smithy shape ``com.amazonaws.mq#DescribeConfigurationRevisionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mq.types.__string
    import capo_mq.types.__timestamp_iso8601


class DescribeConfigurationRevisionResponse(TypedDict, closed=True):
    configuration_id: NotRequired["capo_mq.types.__string.__string"]
    """<p>Required. The unique ID that Amazon MQ generates for the configuration.</p>"""
    created: NotRequired["capo_mq.types.__timestamp_iso8601.__timestampIso8601"]
    """<p>Required. The date and time of the configuration.</p>"""
    data: NotRequired["capo_mq.types.__string.__string"]
    """<p>Amazon MQ for ActiveMQ: the base64-encoded XML configuration. Amazon MQ for RabbitMQ: base64-encoded Cuttlefish.</p>"""
    description: NotRequired["capo_mq.types.__string.__string"]
    """<p>The description of the configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeConfigurationRevisionResponse) -> dict:
    out: dict = {}
    if "configuration_id" in value:
        out["configurationId"] = value["configuration_id"]
    if "created" in value:
        import capo_mq.types.__timestamp_iso8601

        out["created"] = capo_mq.types.__timestamp_iso8601.serialize_json(
            value["created"]
        )
    if "data" in value:
        out["data"] = value["data"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> DescribeConfigurationRevisionResponse:
    out: DescribeConfigurationRevisionResponse = {}  # type: ignore[typeddict-item]
    if "configurationId" in data:
        out["configuration_id"] = data["configurationId"]
    if "created" in data:
        import capo_mq.types.__timestamp_iso8601

        out["created"] = capo_mq.types.__timestamp_iso8601.deserialize_json(
            data["created"]
        )
    if "data" in data:
        out["data"] = data["data"]
    if "description" in data:
        out["description"] = data["description"]
    return out
