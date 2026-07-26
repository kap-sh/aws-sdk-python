"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#OriginationRoute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.origination_route_priority
    import capo_chime_sdk_voice.types.origination_route_protocol
    import capo_chime_sdk_voice.types.origination_route_weight
    import capo_chime_sdk_voice.types.port
    import capo_chime_sdk_voice.types.string


class OriginationRoute(TypedDict, closed=True):
    host: NotRequired["capo_chime_sdk_voice.types.string.String"]
    """<p>The FQDN or IP address to contact for origination traffic.</p>"""
    port: NotRequired["capo_chime_sdk_voice.types.port.Port"]
    """<p>The designated origination route port. Defaults to 5060.</p>"""
    protocol: NotRequired[
        "capo_chime_sdk_voice.types.origination_route_protocol.OriginationRouteProtocol"
    ]
    """<p>The protocol to use for the origination route. Encryption-enabled Amazon Chime SDK Voice Connectors use TCP protocol by default.</p>"""
    priority: NotRequired[
        "capo_chime_sdk_voice.types.origination_route_priority.OriginationRoutePriority"
    ]
    """<p>The priority associated with the host, with 1 being the highest priority. Higher priority hosts are attempted first.</p>"""
    weight: NotRequired[
        "capo_chime_sdk_voice.types.origination_route_weight.OriginationRouteWeight"
    ]
    """<p>The weight assigned to an origination route. When hosts have equal priority, calls are distributed between them based on their relative weights.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OriginationRoute) -> dict:
    out: dict = {}
    if "host" in value:
        out["Host"] = value["host"]
    if "port" in value:
        out["Port"] = value["port"]
    if "protocol" in value:
        import capo_chime_sdk_voice.types.origination_route_protocol

        out["Protocol"] = (
            capo_chime_sdk_voice.types.origination_route_protocol.serialize_json(
                value["protocol"]
            )
        )
    if "priority" in value:
        out["Priority"] = value["priority"]
    if "weight" in value:
        out["Weight"] = value["weight"]
    return out


def deserialize_json(data: dict) -> OriginationRoute:
    out: OriginationRoute = {}  # type: ignore[typeddict-item]
    if "Host" in data:
        out["host"] = data["Host"]
    if "Port" in data:
        out["port"] = data["Port"]
    if "Protocol" in data:
        import capo_chime_sdk_voice.types.origination_route_protocol

        out["protocol"] = (
            capo_chime_sdk_voice.types.origination_route_protocol.deserialize_json(
                data["Protocol"]
            )
        )
    if "Priority" in data:
        out["priority"] = data["Priority"]
    if "Weight" in data:
        out["weight"] = data["Weight"]
    return out
