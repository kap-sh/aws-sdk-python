"""Generated from Smithy shape ``com.amazonaws.vpclattice#CreateListenerResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.listener_arn
    import aws_sdk_vpc_lattice.types.listener_id
    import aws_sdk_vpc_lattice.types.listener_name
    import aws_sdk_vpc_lattice.types.listener_protocol
    import aws_sdk_vpc_lattice.types.port
    import aws_sdk_vpc_lattice.types.rule_action
    import aws_sdk_vpc_lattice.types.service_arn
    import aws_sdk_vpc_lattice.types.service_id


class CreateListenerResponse(TypedDict):
    arn: NotRequired["aws_sdk_vpc_lattice.types.listener_arn.ListenerArn"]
    """<p>The Amazon Resource Name (ARN) of the listener.</p>"""
    id: NotRequired["aws_sdk_vpc_lattice.types.listener_id.ListenerId"]
    """<p>The ID of the listener.</p>"""
    name: NotRequired["aws_sdk_vpc_lattice.types.listener_name.ListenerName"]
    """<p>The name of the listener.</p>"""
    protocol: NotRequired[
        "aws_sdk_vpc_lattice.types.listener_protocol.ListenerProtocol"
    ]
    """<p>The protocol of the listener.</p>"""
    port: NotRequired["aws_sdk_vpc_lattice.types.port.Port"]
    """<p>The port number of the listener.</p>"""
    service_arn: NotRequired["aws_sdk_vpc_lattice.types.service_arn.ServiceArn"]
    """<p>The Amazon Resource Name (ARN) of the service.</p>"""
    service_id: NotRequired["aws_sdk_vpc_lattice.types.service_id.ServiceId"]
    """<p>The ID of the service.</p>"""
    default_action: NotRequired["aws_sdk_vpc_lattice.types.rule_action.RuleAction"]
    """<p>The action for the default rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateListenerResponse) -> dict:
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
        import aws_sdk_vpc_lattice.types.rule_action

        out["defaultAction"] = aws_sdk_vpc_lattice.types.rule_action.serialize_json(
            value["default_action"]
        )
    return out


def deserialize_json(data: dict) -> CreateListenerResponse:
    out: CreateListenerResponse = {}  # type: ignore[typeddict-item]
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
        import aws_sdk_vpc_lattice.types.rule_action

        out["default_action"] = aws_sdk_vpc_lattice.types.rule_action.deserialize_json(
            data["defaultAction"]
        )
    return out
