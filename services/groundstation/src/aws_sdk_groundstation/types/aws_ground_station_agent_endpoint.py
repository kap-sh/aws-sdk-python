"""Generated from Smithy shape ``com.amazonaws.groundstation#AwsGroundStationAgentEndpoint``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.agent_status
    import aws_sdk_groundstation.types.audit_results
    import aws_sdk_groundstation.types.connection_details
    import aws_sdk_groundstation.types.ranged_connection_details
    import aws_sdk_groundstation.types.safe_name


class AwsGroundStationAgentEndpoint(TypedDict):
    name: "aws_sdk_groundstation.types.safe_name.SafeName"
    """<p>Name string associated with AgentEndpoint. Used as a human-readable identifier for AgentEndpoint.</p>"""
    egress_address: "aws_sdk_groundstation.types.connection_details.ConnectionDetails"
    """<p>The egress address of AgentEndpoint.</p>"""
    ingress_address: (
        "aws_sdk_groundstation.types.ranged_connection_details.RangedConnectionDetails"
    )
    """<p>The ingress address of AgentEndpoint.</p>"""
    agent_status: NotRequired["aws_sdk_groundstation.types.agent_status.AgentStatus"]
    """<p>The status of AgentEndpoint.</p>"""
    audit_results: NotRequired["aws_sdk_groundstation.types.audit_results.AuditResults"]
    """<p>The results of the audit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsGroundStationAgentEndpoint) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_groundstation.types.connection_details

    out["egressAddress"] = (
        aws_sdk_groundstation.types.connection_details.serialize_json(
            value["egress_address"]
        )
    )
    import aws_sdk_groundstation.types.ranged_connection_details

    out["ingressAddress"] = (
        aws_sdk_groundstation.types.ranged_connection_details.serialize_json(
            value["ingress_address"]
        )
    )
    if "agent_status" in value:
        import aws_sdk_groundstation.types.agent_status

        out["agentStatus"] = aws_sdk_groundstation.types.agent_status.serialize_json(
            value["agent_status"]
        )
    if "audit_results" in value:
        import aws_sdk_groundstation.types.audit_results

        out["auditResults"] = aws_sdk_groundstation.types.audit_results.serialize_json(
            value["audit_results"]
        )
    return out


def deserialize_json(data: dict) -> AwsGroundStationAgentEndpoint:
    out: AwsGroundStationAgentEndpoint = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AwsGroundStationAgentEndpoint.name required")
    if "egressAddress" in data:
        import aws_sdk_groundstation.types.connection_details

        out["egress_address"] = (
            aws_sdk_groundstation.types.connection_details.deserialize_json(
                data["egressAddress"]
            )
        )
    else:
        raise DeserializationError(
            "AwsGroundStationAgentEndpoint.egress_address required"
        )
    if "ingressAddress" in data:
        import aws_sdk_groundstation.types.ranged_connection_details

        out["ingress_address"] = (
            aws_sdk_groundstation.types.ranged_connection_details.deserialize_json(
                data["ingressAddress"]
            )
        )
    else:
        raise DeserializationError(
            "AwsGroundStationAgentEndpoint.ingress_address required"
        )
    if "agentStatus" in data:
        import aws_sdk_groundstation.types.agent_status

        out["agent_status"] = aws_sdk_groundstation.types.agent_status.deserialize_json(
            data["agentStatus"]
        )
    if "auditResults" in data:
        import aws_sdk_groundstation.types.audit_results

        out["audit_results"] = (
            aws_sdk_groundstation.types.audit_results.deserialize_json(
                data["auditResults"]
            )
        )
    return out
