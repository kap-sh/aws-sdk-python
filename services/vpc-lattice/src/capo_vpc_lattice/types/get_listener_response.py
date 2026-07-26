"""Generated from Smithy shape ``com.amazonaws.vpclattice#GetListenerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.listener_arn
    import capo_vpc_lattice.types.listener_id
    import capo_vpc_lattice.types.listener_name
    import capo_vpc_lattice.types.listener_protocol
    import capo_vpc_lattice.types.port
    import capo_vpc_lattice.types.rule_action
    import capo_vpc_lattice.types.service_arn
    import capo_vpc_lattice.types.service_id
    import capo_vpc_lattice.types.timestamp


class GetListenerResponse(TypedDict, closed=True):
    arn: NotRequired["capo_vpc_lattice.types.listener_arn.ListenerArn"]
    """<p>The Amazon Resource Name (ARN) of the listener.</p>"""
    id: NotRequired["capo_vpc_lattice.types.listener_id.ListenerId"]
    """<p>The ID of the listener.</p>"""
    name: NotRequired["capo_vpc_lattice.types.listener_name.ListenerName"]
    """<p>The name of the listener.</p>"""
    protocol: NotRequired["capo_vpc_lattice.types.listener_protocol.ListenerProtocol"]
    """<p>The listener protocol.</p>"""
    port: NotRequired["capo_vpc_lattice.types.port.Port"]
    """<p>The listener port.</p>"""
    service_arn: NotRequired["capo_vpc_lattice.types.service_arn.ServiceArn"]
    """<p>The Amazon Resource Name (ARN) of the service.</p>"""
    service_id: NotRequired["capo_vpc_lattice.types.service_id.ServiceId"]
    """<p>The ID of the service.</p>"""
    default_action: NotRequired["capo_vpc_lattice.types.rule_action.RuleAction"]
    """<p>The actions for the default listener rule.</p>"""
    created_at: NotRequired["capo_vpc_lattice.types.timestamp.Timestamp"]
    """<p>The date and time that the listener was created, in ISO-8601 format.</p>"""
    last_updated_at: NotRequired["capo_vpc_lattice.types.timestamp.Timestamp"]
    """<p>The date and time that the listener was last updated, in ISO-8601 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetListenerResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "protocol" in value:
        out["protocol"] = value["protocol"]
    if "port" in value:
        out["port"] = value["port"]
    if "service_arn" in value:
        out["serviceArn"] = value["service_arn"]
    if "service_id" in value:
        out["serviceId"] = value["service_id"]
    if "default_action" in value:
        import capo_vpc_lattice.types.rule_action

        out["defaultAction"] = capo_vpc_lattice.types.rule_action.serialize_json(
            value["default_action"]
        )
    if "created_at" in value:
        import capo_vpc_lattice.types.timestamp

        out["createdAt"] = capo_vpc_lattice.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import capo_vpc_lattice.types.timestamp

        out["lastUpdatedAt"] = capo_vpc_lattice.types.timestamp.serialize_json(
            value["last_updated_at"]
        )
    return out


def deserialize_json(data: dict) -> GetListenerResponse:
    out: GetListenerResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "protocol" in data:
        out["protocol"] = data["protocol"]
    if "port" in data:
        out["port"] = data["port"]
    if "serviceArn" in data:
        out["service_arn"] = data["serviceArn"]
    if "serviceId" in data:
        out["service_id"] = data["serviceId"]
    if "defaultAction" in data:
        import capo_vpc_lattice.types.rule_action

        out["default_action"] = capo_vpc_lattice.types.rule_action.deserialize_json(
            data["defaultAction"]
        )
    if "createdAt" in data:
        import capo_vpc_lattice.types.timestamp

        out["created_at"] = capo_vpc_lattice.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "lastUpdatedAt" in data:
        import capo_vpc_lattice.types.timestamp

        out["last_updated_at"] = capo_vpc_lattice.types.timestamp.deserialize_json(
            data["lastUpdatedAt"]
        )
    return out
