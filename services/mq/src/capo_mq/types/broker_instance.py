"""Generated from Smithy shape ``com.amazonaws.mq#BrokerInstance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mq.types.__list_of__string
    import capo_mq.types.__string


class BrokerInstance(TypedDict, closed=True):
    console_url: NotRequired["capo_mq.types.__string.__string"]
    """<p>The brokers web console URL.</p>"""
    endpoints: NotRequired["capo_mq.types.__list_of__string.__listOf__string"]
    """<p>The broker's wire-level protocol endpoints.</p>"""
    ip_address: NotRequired["capo_mq.types.__string.__string"]
    """<p>The IP address of the Elastic Network Interface (ENI) attached to the broker. Does not apply to RabbitMQ brokers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BrokerInstance) -> dict:
    out: dict = {}
    if "console_url" in value:
        out["consoleURL"] = value["console_url"]
    if "endpoints" in value:
        import capo_mq.types.__list_of__string

        out["endpoints"] = capo_mq.types.__list_of__string.serialize_json(
            value["endpoints"]
        )
    if "ip_address" in value:
        out["ipAddress"] = value["ip_address"]
    return out


def deserialize_json(data: dict) -> BrokerInstance:
    out: BrokerInstance = {}  # type: ignore[typeddict-item]
    if "consoleURL" in data:
        out["console_url"] = data["consoleURL"]
    if "endpoints" in data:
        import capo_mq.types.__list_of__string

        out["endpoints"] = capo_mq.types.__list_of__string.deserialize_json(
            data["endpoints"]
        )
    if "ipAddress" in data:
        out["ip_address"] = data["ipAddress"]
    return out
