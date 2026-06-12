"""Generated from Smithy shape ``com.amazonaws.securityhub#Action``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_api_call_action
    import aws_sdk_securityhub.types.dns_request_action
    import aws_sdk_securityhub.types.network_connection_action
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.port_probe_action


class Action(TypedDict):
    action_type: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The type of action that was detected. The possible action types are:</p> <ul> <li> <p> <code>NETWORK_CONNECTION</code> </p> </li> <li> <p> <code>AWS_API_CALL</code> </p> </li> <li> <p> <code>DNS_REQUEST</code> </p> </li> <li> <p> <code>PORT_PROBE</code> </p> </li> </ul>"""
    network_connection_action: NotRequired[
        "aws_sdk_securityhub.types.network_connection_action.NetworkConnectionAction"
    ]
    """<p>Included if <code>ActionType</code> is <code>NETWORK_CONNECTION</code>. Provides details about the network connection that was detected.</p>"""
    aws_api_call_action: NotRequired[
        "aws_sdk_securityhub.types.aws_api_call_action.AwsApiCallAction"
    ]
    """<p>Included if <code>ActionType</code> is <code>AWS_API_CALL</code>. Provides details about the API call that was detected. </p>"""
    dns_request_action: NotRequired[
        "aws_sdk_securityhub.types.dns_request_action.DnsRequestAction"
    ]
    """<p>Included if <code>ActionType</code> is <code>DNS_REQUEST</code>. Provides details about the DNS request that was detected. </p>"""
    port_probe_action: NotRequired[
        "aws_sdk_securityhub.types.port_probe_action.PortProbeAction"
    ]
    """<p>Included if <code>ActionType</code> is <code>PORT_PROBE</code>. Provides details about the port probe that was detected. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Action) -> dict:
    out: dict = {}
    if "action_type" in value:
        out["ActionType"] = value["action_type"]
    if "network_connection_action" in value:
        import aws_sdk_securityhub.types.network_connection_action

        out["NetworkConnectionAction"] = (
            aws_sdk_securityhub.types.network_connection_action.serialize_json(
                value["network_connection_action"]
            )
        )
    if "aws_api_call_action" in value:
        import aws_sdk_securityhub.types.aws_api_call_action

        out["AwsApiCallAction"] = (
            aws_sdk_securityhub.types.aws_api_call_action.serialize_json(
                value["aws_api_call_action"]
            )
        )
    if "dns_request_action" in value:
        import aws_sdk_securityhub.types.dns_request_action

        out["DnsRequestAction"] = (
            aws_sdk_securityhub.types.dns_request_action.serialize_json(
                value["dns_request_action"]
            )
        )
    if "port_probe_action" in value:
        import aws_sdk_securityhub.types.port_probe_action

        out["PortProbeAction"] = (
            aws_sdk_securityhub.types.port_probe_action.serialize_json(
                value["port_probe_action"]
            )
        )
    return out


def deserialize_json(data: dict) -> Action:
    out: Action = {}  # type: ignore[typeddict-item]
    if "ActionType" in data:
        out["action_type"] = data["ActionType"]
    if "NetworkConnectionAction" in data:
        import aws_sdk_securityhub.types.network_connection_action

        out["network_connection_action"] = (
            aws_sdk_securityhub.types.network_connection_action.deserialize_json(
                data["NetworkConnectionAction"]
            )
        )
    if "AwsApiCallAction" in data:
        import aws_sdk_securityhub.types.aws_api_call_action

        out["aws_api_call_action"] = (
            aws_sdk_securityhub.types.aws_api_call_action.deserialize_json(
                data["AwsApiCallAction"]
            )
        )
    if "DnsRequestAction" in data:
        import aws_sdk_securityhub.types.dns_request_action

        out["dns_request_action"] = (
            aws_sdk_securityhub.types.dns_request_action.deserialize_json(
                data["DnsRequestAction"]
            )
        )
    if "PortProbeAction" in data:
        import aws_sdk_securityhub.types.port_probe_action

        out["port_probe_action"] = (
            aws_sdk_securityhub.types.port_probe_action.deserialize_json(
                data["PortProbeAction"]
            )
        )
    return out
