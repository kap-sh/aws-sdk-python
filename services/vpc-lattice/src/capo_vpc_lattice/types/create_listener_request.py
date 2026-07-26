"""Generated from Smithy shape ``com.amazonaws.vpclattice#CreateListenerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_vpc_lattice.errors import DeserializationError

if TYPE_CHECKING:
    import capo_vpc_lattice.types.client_token
    import capo_vpc_lattice.types.listener_name
    import capo_vpc_lattice.types.listener_protocol
    import capo_vpc_lattice.types.port
    import capo_vpc_lattice.types.rule_action
    import capo_vpc_lattice.types.service_identifier
    import capo_vpc_lattice.types.tag_map


class CreateListenerRequest(TypedDict, closed=True):
    service_identifier: "capo_vpc_lattice.types.service_identifier.ServiceIdentifier"
    """<p>The ID or ARN of the service.</p>"""
    name: "capo_vpc_lattice.types.listener_name.ListenerName"
    """<p>The name of the listener. A listener name must be unique within a service. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.</p>"""
    protocol: "capo_vpc_lattice.types.listener_protocol.ListenerProtocol"
    """<p>The listener protocol.</p>"""
    port: NotRequired["capo_vpc_lattice.types.port.Port"]
    """<p>The listener port. You can specify a value from 1 to 65535. For HTTP, the default is 80. For HTTPS, the default is 443.</p>"""
    default_action: "capo_vpc_lattice.types.rule_action.RuleAction"
    """<p>The action for the default rule. Each listener has a default rule. The default rule is used if no other rules match.</p>"""
    client_token: NotRequired["capo_vpc_lattice.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>"""
    tags: NotRequired["capo_vpc_lattice.types.tag_map.TagMap"]
    """<p>The tags for the listener.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateListenerRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["protocol"] = value["protocol"]
    if "port" in value:
        out["port"] = value["port"]
    import capo_vpc_lattice.types.rule_action

    out["defaultAction"] = capo_vpc_lattice.types.rule_action.serialize_json(
        value["default_action"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_vpc_lattice.types.tag_map

        out["tags"] = capo_vpc_lattice.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateListenerRequest:
    out: CreateListenerRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateListenerRequest.name required")
    if "protocol" in data:
        out["protocol"] = data["protocol"]
    else:
        raise DeserializationError("CreateListenerRequest.protocol required")
    if "port" in data:
        out["port"] = data["port"]
    if "defaultAction" in data:
        import capo_vpc_lattice.types.rule_action

        out["default_action"] = capo_vpc_lattice.types.rule_action.deserialize_json(
            data["defaultAction"]
        )
    else:
        raise DeserializationError("CreateListenerRequest.default_action required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "tags" in data:
        import capo_vpc_lattice.types.tag_map

        out["tags"] = capo_vpc_lattice.types.tag_map.deserialize_json(data["tags"])
    return out
